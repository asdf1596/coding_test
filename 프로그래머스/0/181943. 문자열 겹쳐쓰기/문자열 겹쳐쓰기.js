function solution(my_string, overwrite_string, s) {
    s = parseInt(s)
    if (!overwrite_string) {
        return "Invalid input";
    }
    my_string = my_string.split('');
    
    for(let a=s;a<overwrite_string.length+s;a++){
        my_string[a] = overwrite_string[a-s]
    }
    var answer = my_string.join('');
    return answer;
}
solution()