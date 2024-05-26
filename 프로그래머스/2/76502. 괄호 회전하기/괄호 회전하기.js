function try3(lista){
    lista = lista.slice();
    let try1 = [];
    try1.push(lista[0]);
    lista.shift();
    for(let c = 0;c<lista.length;c++){
        //console.log(lista, try1, lista[c]);
        if(try1[try1.length-1] == "(" && lista[c] == ")"){
            try1.pop();
            //console.log(try1);
            continue;
        }
        else if(try1[try1.length-1] == "[" &&lista[c] == "]"){
            try1.pop();
            //console.log(try1);
            continue;
        }
        else if(try1[try1.length-1] == "{" && lista[c] == "}"){
            try1.pop();
            //console.log(try1);
            continue;
        }
        else if(lista[c] == "{"){
            try1.push(lista[c])
            //console.log(try1);
        }else if(lista[c] == "(") {
            try1.push(lista[c]);
            //console.log(try1);
        }else if(lista[c] == "[") {
            try1.push(lista[c]);
            //console.log(try1);
        }else{
            //console.log("끝");
            //console.log("실패");
            return 0;
        }
    }
    //console.log("끝");
    if(try1.length == 0){
        //console.log("성공");
        return 1;
    }
    if(try1.length != 0){ 
        //console.log("실패");
        return 0;
    }
}
function solution(s) {
    var answer = 0;
    s = s.split("");
    let try5 = "";
    for(let a = 0;a<s.length;a++){
        if(s[0] == "}" || s[0] == ")" || s[0] == "]"){
            try5 = s.shift();
            s.push(try5);
            //console.log("끝");
            //console.log("실패");
            continue;
        };
        answer=answer+try3(s);
        try5 = s.shift();
        s.push(try5);
    }
    return answer;
}
