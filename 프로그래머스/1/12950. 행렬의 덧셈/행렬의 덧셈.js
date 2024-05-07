function solution(arr1, arr2) {
    var answer = [];
    let try1 = [];
    for(let a = 0;a<arr1.length;a++){
        for(let b = 0;b<arr1[0].length;b++){
            try1.push(arr1[a][b]+arr2[a][b]);
        }
        answer.push(try1);
        try1 = [];
    }
    return answer;
}