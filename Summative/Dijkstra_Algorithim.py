def graph():
    '''
    graph() --> dictionary
    Returns a dictionary with all the nodes that are have connections to each
    other.
    '''
    
    graph = {'1': ['2', '4'], '2': ['1', '3', '5'], '3': ['2', '10'], '4': ['1', '5', '8'], '5': ['4', '2', '6'], '6': ['5', '9', '7'], '7': ['6', '8', '38'], '8': ['7', '4'], '9': ['6', '10', '11'], '10': ['3', '9', '21'], '11': ['9', '12'], '12': ['11', '13'], '13': ['12', '14', '15'], '14': ['13', '37'], '15': ['13', '33'], '16': ['33', '17'], '17': ['16', '18', '32'], '18': ['17', '19'], '19': ['18', '20'], '20': ['19', '21', '27'], '21': ['10', '20', '22'], '22': ['21', '23'], '23': ['22', '24', '26'], '24': ['23', '25'], '25': ['24', '26', '29'], '26': ['25', '23', '27'], '27': ['26', '28', '20'], '28': ['27', '29', '30'], '29': ['25', '28'], '30': ['31', '28', '55', '62'], '31': ['30', '32', '52'], '32': ['31', '17'], '33': ['15', '16', '34'], '34': ['33', '35', '36'], '35': ['34'], '36': ['34'], '37': ['14', '53', '38'], '38': ['7', '37', '39', '61'], '39': ['38', '40', '45'], '40': ['39', '41'], '41': ['40', '42', '44'], '42': ['41', '43'], '43': ['42', '44', '48'], '44': ['41', '45', '43'], '45': ['44', '39', '46'], '46': ['53', '45', '47'], '47': ['46', '48', '50'], '48': ['47', '43', '49'], '49': ['48', '50', '59'], '50': ['49', '47', '51'], '51': ['52', '50', '54'], '52': ['51', '31', '53'], '53': ['37', '52', '46'], '54': ['51', '55', '58'], '55': ['54', '30', '56'], '56': ['55', '57'], '57': ['56', '58', '60'], '58': ['57', '54', '59'], '59': ['58', '60', '49'], '60': ['57', '59'], '61': ['38'], '62': ['30']}
    
    return graph


def node_coordinates():
    '''
    node_coordinates() --> dictionary
    Returns a dictionary with of the nodes' coordinates. The key is the node and
    the values are the coordinates
    '''
    
    node_coordinates = {'1':(2,2), '2':(5,2), '4':(2,4), '5':(5,4), '6':(5,5), '7':(5,7), '3':(9,2), '8':(2,7), '9':(7,5), '10':(9,5), '11':(7,7), '12':(9,7), '13':(9,9), '14':(7,9), '15':(9,10), '16':(11,10), '17':(11,9), '18':(11,7), '19':(13,7), '20':(13,5), '21':(11,5), '22':(11,2), '23':(15,2), '24':(18,2), '25':(18,4), '26':(15,4), '27':(15,5), '28':(15,7), '29':(18,7), '30':(15,11), '31':(13,11), '32':(13,9), '33':(10,10), '34':(10,12), '35':(9,12), '36':(11,12), '37':(7,11), '38':(5,11), '39':(5,15), '40':(2,15), '41':(2,18), '42':(2,20), '43':(5,20), '44':(5,18), '45':(5,17), '46':(7,17), '47':(9,17), '48':(9,20), '49':(11,20), '50':(11,17), '51':(13,17), '52':(13,14), '53':(7,14), '54':(15,17), '55':(15,15), '56':(18,15), '57':(18,18), '58':(15,18), '59':(15,20), '60':(18,20), '61': (1,11), '62': (19,11)}
    
    return node_coordinates


def rev_node_coordinates():
    '''
    rev_node_coordinates() --> dictionary
    Same as node_coordinates() but reversed. The key is the coordinates and the
    values are the nodes.
    '''
    
    rev_node_coordinates = {(2,2):'1',(5,2):'2',(2,4):'4',(5,4):'5',(5,5):'6',(5,7):'7',(9,2):'3',(2,7):'8',(7,5):'9',(9,5):'10',(7,7):'11',(9,7):'12',(9,9):'13',(7,9):'14',(9,10):'15',(11,10):'16',(11,9):'17',(11,7):'18',(13,7):'19',(13,5):'20',(11,5):'21',(11,2):'22',(15,2):'23',(18,2):'24',(18,4):'25',(15,4):'26',(15,5):'27',(15,7):'28',(18,7):'29',(15,11):'30',(13,11):'31',(13,9):'32',(10,10):'33',(10,12):'34',(9,12):'35',(11,12):'36',(7,11):'37',(5,11):'38',(5,15):'39',(2,15):'40',(2,18):'41',(2,20):'42',(5,20):'43',(5,18):'44',(5,17):'45',(7,17):'46',(9,17):'47',(9,20):'48',(11,20):'49',(11,17):'50',(13,17):'51',(13,14):'52',(7,14):'53',(15,17):'54',(15,15):'55',(18,15):'56',(18,18):'57',(15,18):'58',(15,20):'59',(18,20):'60',(1,11):'61',(19,11):'62'}
    
    return rev_node_coordinates 



def find_distance(vertex_start, vertex_end):
    '''
    find_distance(vertex1, vertex2) --> INT
    Returns the distance between two nodes that have a connection to one another.
    Returns None if the key does not exist
    '''
    
    edges = {'1,2':3,'1,4':2,'2,3':4,'2,5':2,'3,10':3,'4,5':3,'4,8':3,'5,6':1,'6,7':2,'6,9':2,'7,8':3,'7,38':4,'9,10':2,'9,11':2,'10,21':2,'11,12':2,'12,13':2,'13,14':2,'13,15':1,'14,37':2,'15,33':1,'16,17':1,'16,33':1,'17,18':2,'17,32':2,'18,19':2,'19,20':2,'20,21':2,'20,27':2,'21,22':3,'22,23':4,'23,24':3,'23,26':2,'24,25':2,'25,26':3,'25,29':3,'26,27':1,'27,28':2,'28,29':3,'28,30':4,'30,31':2,'30,55':4,'31,32':2,'31,52':3,'33,34':2,'34,35':1,'34,36':1,'37,38':2,'37,53':3,'38,39':4,'39,40':3,'39,45':2,'40,41':3,'41,42':2,'41,44':3,'42,43':3,'43,44':2,'43,48':4,'44,45':1,'45,46':2,'46,47':2,'46,53':3,'47,48':3,'47,50':2,'48,49':2,'49,50':3,'49,59':4,'50,51':2,'51,52':3,'51,54':2,'52,53':6,'54,55':2,'54,58':1,'55,56':3,'56,57':3,'57,58':3,'57,60':2,'58,59':2,'59,60':3,'38,61':4,'30,62':4}
    
    key = vertex_start +','+ vertex_end
    
    if edges.has_key(key):
        return edges[key]
    
    else:
        key = vertex_end +','+ vertex_start
        
        if edges.has_key(key):
            return edges[key]
        
        else:
            return None

        
        
def dijkstra(graph, source, target, find_shortest_path = True):
    '''
    dijkstra(graph, source, target, find_shortest_path = True) --> List or INT
    Returns the shortest path to the target if find_shortest_path is True. If 
    False it will return the node that is farthest from the source.
    '''
    
    INF = 10000
    NOT_DEFINED = -1
    distance = {}
    
    previous = {}
    Q = set()
    path = []
    
    # for each vertex makes the distance and previous connection infitity and
    # un-defined respectfully
    for vertex in graph:
        
        distance[vertex] = INF
        previous[vertex] = NOT_DEFINED
        Q.add(vertex)
    
    
    distance[source] = 0
    
    
    while len(Q) > 0:
        
        dist_min = 2 * INF
        
        for vertex in Q:
            
            if distance[vertex] < dist_min:
                dist_min = distance[vertex]
                vertex_min = vertex
        
                
        if dist_min == INF: # returns 0 if graph has no link
            return 0 
        
        
        # finds the shortest path between source and target
        if vertex_min == target and find_shortest_path:
            vrtx_path = target
            
            while previous[vrtx_path] != NOT_DEFINED:
                path = [vrtx_path] + path
                vrtx_path = previous[vrtx_path]
                
            path = [source] + path
            return path
        
        
        else: 
            # if the vertex_min is not equal to the target then it finds the 
            # next vertex_min
                
            Q.remove(vertex_min)
            
            for neighbour in graph[vertex_min]:
                if neighbour in Q:
                    alt = distance[vertex_min] + find_distance(vertex_min, neighbour) # adds the distances together
                
                if alt < distance[neighbour]:
                    distance[neighbour] = alt
                    previous[neighbour] = vertex_min
    
                    
    
    # finds the node farthest from the source
    if find_shortest_path == False:
        
        dist = NOT_DEFINED
        farthest_vertex = source
        for vertex in distance:
            
            if distance[vertex] > dist:
                dist = distance[vertex]
                farthest_vertex = vertex
        
        return farthest_vertex
