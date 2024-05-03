func solution(n int) int {
    if n<=7{
    return 1}
    if n%7==0{
        return n/7
    }
    return n/7+1
}