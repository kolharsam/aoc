package org.example

import java.io.File

fun day3() {
    val input = File("inputs/input3").readLines()
    val regexP1 = Regex("""mul\((\d+),(\d+)\)""")
    val regexP2 = Regex("""mul\((\d+),(\d+)\)|do\(\)|don't\(\)""")

    var p1 = 0
    var p2 = 0
    var addVals = true

    for (line in input) {
        val matchesP1 = regexP1.findAll(line)
        for (match in matchesP1) {
            val (_, a, b) = match.groupValues
            p1 += (Integer.parseInt(a) * Integer.parseInt(b))
        }
        val matchesP2 = regexP2.findAll(line)
        for (match in matchesP2) {
            val (comm, a, b) = match.groupValues
            if (comm == "don't()") {
                addVals = false
                continue
            } else if (comm == "do()") {
                addVals = true
                continue
            }
            if (addVals) {
                p2 += (Integer.parseInt(a) * Integer.parseInt(b))
            }
        }
    }

    println(p1)
    println(p2)
}