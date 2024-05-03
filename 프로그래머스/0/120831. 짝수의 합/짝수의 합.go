func solution(n int) int {
    ans := 0
    for n!=0{
        if n%2 == 0{
            ans+=n}
            n--
    }
    return ans
}