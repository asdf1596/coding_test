func solution(my_string string) string {
    ans := ""
    var lis []byte  // 타입을 []byte로 수정
    for i := 0; i < len(my_string); i++ {
        lis = append(lis, my_string[len(my_string)-1-i])
    }
    for i := 0; i < len(lis); i++ {
        ans += string(lis[i])
    }
    return ans
}
