adjacencyList ={
    'A':['B','F'],
    'B':['A','F','C'],
    'C':['B','E','D'],
    'D':['C','E'],
    'E':['D','C','F'],
    'F':['A','B','E']
}

def travDFSIterative = function(graph,start):
    const output =[];
    const visited ={};
    const stack = [start];
    visited[start] = true;
    let current;
    while(stack.length>0){
        current= stack.pop();
        output.push(current);
        const neighbours = graph[current];
        for(let i=0;i<neighbours.length;i++){
            if(!visited[neighbours[i]]){
                stack.push(neighbours[i]);
                visited[neighbours[i]]=true;
            }
        }
    }
    return output;


travDFSIterative(adjacencyList,'A');