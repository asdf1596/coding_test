function solution(id_list, report, k) {


    let id = id_list;
    let re = report;
    var answer = [];
    var list=[];
    var list1 = [];
    var list2 = [];
    var list3 = [];
    for (let a = 0;a<id.length;a++){
        answer.push(0)
    }
    for (let a= 0;a<id.length;a++){
        list.push([])
    }
    for (let a=0;a<re.length;a++){
        list1.push(re[a].split(' ')[0])
        list2.push(re[a].split(' ')[1])
    }
    for(let a=0;a<id.length;a++){
        for(let b = 0;b<list1.length;b++){
            if(id[a]==list2[b]){
                list[a].push(list1[b])
            }
        }
    }
    for(let a = 0;a<list.length;a++){
        const set = new Set(list[a]);
        list[a] = [...set];
        if(list[a].length>=k){
            list[a] = 1
        }else{
            list[a]=0
        }
    }
    let list4 = []
    let list5 = []
    for (let a= 0;a<id.length;a++){
        list4.push([])
    }
    for(let a=0;a<id.length;a++){
        for(let b = 0;b<list2.length;b++){
            if(id[a]==list1[b]){
                list4[a].push(list2[b])
            }
        }
    }
    for(let a = 0;a<list4.length;a++){
        const set = new Set(list4[a]);
        list4[a] = [...set];
    }
    for(let a=0;a<id.length;a++){
        list5.push({name:id[a],value:list[a]})
    }
    function isBanned(name,element)  {
        for(let a = 0;a<element.length;a++){
            if(name == element[a].name){
                return element[a].value
            }
        }
    }
    for(let a= 0;a<id.length;a++){
        for(let b = 0;b<list4[a].length;b++){
            answer[a]+=isBanned(list4[a][b], list5)
        }
    }
    console.log(list)
    console.log(list4)
    console.log(list5)
    return answer;
}