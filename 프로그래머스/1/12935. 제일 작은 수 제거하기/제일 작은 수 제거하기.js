function solution(arr) {
    let b = 99999999;
    let c = 0;
    for(let a =0;a<arr.length;a++){
        if(arr[a]<b){
            c = a;
            b = arr[a];
        }
    }
    arr.splice(c,1);
    if(arr.length == 0){
        return[-1];
    }
    return arr;
}