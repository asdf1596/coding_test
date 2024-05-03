func solution(numbers []int) float64 {
    ans := 0.0
    length := len(numbers)
    for i := 0;i<length;i++{
        ans+=float64(numbers[i])
    }
    return (ans/float64(length))
}