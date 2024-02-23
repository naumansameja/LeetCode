function repeated(s) {
    var cur_s = ""
    for (let i=0; i<s.length-1; i++) {   
        cur_s += s[i]
        var n = cur_s.repeat(parseInt(s.length / cur_s.length))
        if (n === s){
            return true
        } 
    
    }
    return false
}
console.log(repeated("aba"))