function solution(n) {
    n = n.toString();
    var answer = 0;
    let a = n.split("");
    for(let b = 0;b<a.length;b++){
        a[b] = parseInt(a[b]);
    }
    a.sort(function(c, b)  {
  return b - c;
});
    a[0] = a[0].toString();
    for(let b = 1;b<a.length;b++){
        a[0] += a[b].toString();
    }
    console.log(a);
    answer = parseInt(a[0]);
    return answer;
}