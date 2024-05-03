function solution(w) {
    var answer = [];
    var try1 = [];
    var xsmall = 50;
    var ysmall = 50;
    var xbig = 0;
    var ybig = 0;
    for(let a = 0;a<w.length;a++){
        try1.push(w[a].split(""));
        for(let b=0;b<w[a].length;b++){
            if(w[a][b] == "#"){
                if(a<ysmall){
                    ysmall = a;
                }
                if(a>ybig){
                    ybig = a;
                }
                if(b<xsmall){
                    xsmall = b;
                }
                if(b>xbig){
                    xbig = b;
                }
            }
        }
    }
    answer = [ysmall,xsmall,ybig+1,xbig+1];
    return answer;
}