function solution(absolutes, signs) {
    var b = 0;
    for(let a= 0;a<absolutes.length;a++){
        b+=(absolutes[a] * ((signs[a]) ? 1 : -1));
    }
    return b;
}