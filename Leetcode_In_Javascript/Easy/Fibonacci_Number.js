function fib(n) {
    if (n==0 || n==1){
        return n
    }
    var num = 0
    if (n-1 in d){
        num += d[n-1]
    }
    else {
        d[n-1] = fib(n-1)
        num += d[n-1]
    }
    if (n-2 in d){
        num += d[n-2]
    }
    else {
        d[n-2] = fib(n-2)
        num += d[n-2]
    }
    return num
    
}

var d = {}
console.log(fib(7))