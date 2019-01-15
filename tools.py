# -*- generated by 1.0.12 -*-
import da
PatternExpr_398 = da.pat.ConstantPattern('complete')
PatternExpr_402 = da.pat.FreePattern('q')
PatternExpr_421 = da.pat.TuplePattern([da.pat.ConstantPattern('answer'), da.pat.FreePattern('stach'), da.pat.FreePattern('locWeights')])
PatternExpr_430 = da.pat.FreePattern('s')
_config_object = {}
import igraph
import random
import enum

def genGraphEdges(n):
    numEdges = random.randint(n, (4 * n))
    gr = igraph.Graph(directed=False)
    gr = gr.Erdos_Renyi(n=n, m=numEdges)
    nodes = gr.vs.indices
    tuple_list = []
    for e in gr.es:
        tuple_list.append(e.tuple)
    return tuple_list

class NodeState(enum.Enum):
    sleep = 1
    find = 2
    found = 3
    finished = 4

class EdgeState(enum.Enum):
    branch = 1
    reject = 2
    basic = 3

class Observer(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ObserverReceivedEvent_0', PatternExpr_398, sources=[PatternExpr_402], destinations=None, timestamps=None, record_history=None, handlers=[self._Observer_handler_397]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ObserverReceivedEvent_1', PatternExpr_421, sources=[PatternExpr_430], destinations=None, timestamps=None, record_history=None, handlers=[self._Observer_handler_420])])

    def setup(self, nodes, edges, weights, nodesDic, **rest_497):
        super().setup(nodes=nodes, edges=edges, weights=weights, nodesDic=nodesDic, **rest_497)
        self._state.nodes = nodes
        self._state.edges = edges
        self._state.weights = weights
        self._state.nodesDic = nodesDic
        self._state.receivedAnswers = 0
        self._state.gr = igraph.Graph(directed=False)
        self._state.gr.add_vertices(range(len(self._state.nodes)))
        self._state.gr.add_edges(self._state.edges)
        self._state.gr.es['label'] = self._state.weights
        self._state.gr.vs['label'] = range(len(self._state.nodes))
        self._state.completing = False
        layout = self._state.gr.layout('kk')
        igraph.plot(self._state.gr, layout=layout)
        self._state.graphWeights = []

    def run(self):
        layout = self._state.gr.layout('kk')
        self._state.gr.delete_edges(None)
        self._state.gr.es['label'] = []
        super()._label('_st_label_368', block=False)
        _st_label_368 = 0
        while (_st_label_368 == 0):
            _st_label_368 += 1
            if (self._state.receivedAnswers == len(self._state.nodes)):
                _st_label_368 += 1
            else:
                super()._label('_st_label_368', block=True)
                _st_label_368 -= 1
        self._state.gr.es['label'] = self._state.graphWeights
        igraph.plot(self._state.gr, layout=layout)

    def _Observer_handler_397(self, q):
        if (not self._state.completing):
            self.send('obsQuery', to=self._state.nodes)
            self._state.completing = True
    _Observer_handler_397._labels = None
    _Observer_handler_397._notlabels = None

    def _Observer_handler_420(self, stach, locWeights, s):
        self.output('Observer has received answer from ', self._state.nodesDic[s])
        sourceNum = self._state.nodesDic[s]
        for (dest, st) in stach.items():
            destNum = self._state.nodesDic[dest]
            if ((st == EdgeState.branch) and (not self._state.gr.are_connected(sourceNum, destNum))):
                self._state.gr.add_edges([(sourceNum, destNum)])
                self._state.graphWeights.append(locWeights[dest])
        self._state.receivedAnswers += 1
    _Observer_handler_420._labels = None
    _Observer_handler_420._notlabels = None
