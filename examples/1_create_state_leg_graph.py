import govlytics

def main():

    currlegs = govlytics.gov.legislators.CurrentLegislators()
    graph = govlytics.graph.ops.return_graph()
    govlytics.graph.ops.map_legislators_to_state(graph, currlegs)


if __name__ == '__main__':
    main()
