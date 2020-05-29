package codility

//https://stackoverflow.com/questions/57923558/codility-problem-to-find-optimal-way-for-get-number-equal-to-l-n-or-r-n
//https://stackoverflow.com/questions/53278908/find-shortest-sequence-of-mathematical-operations

fun main() {
    minNumberOfOperations(11)
    println("\n")
}

fun minNumberOfOperations(n: Int) {
    println("N: $n")

    var l = 0
    var r = 1

    val b: String = if (n > 0) Integer.toBinaryString(n - 1) else Integer.toBinaryString(-n)

    println("b: $b")

    for (i in b.length - 1 downTo 0) {
        if (b[i] == (if (n > 0) '0' else '1')) {
            l = 2 * l - r
            println("'L' ==> L: $l, R: $r")
        } else {
            r = 2 * r - l
            println("'R' ==> L: $l, R: $r")
        }
    }

}