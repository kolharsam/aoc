package org.example

import java.io.File

fun day2() {
    val input = File("inputs/input2")
    val reports = mutableListOf<List<Int>>()

    val lines = input.readLines()

    lines.forEach { line ->
        val lineSp = line.split(" ").map { numStr -> Integer.parseInt(numStr) }
        reports.add(
            lineSp
        )
    }

    var p1 = 0
    var p2 = 0
    for (line in reports) {
        if (checkSafetyP1(line)) {
            p1 += 1
        }
        if (checkSafetyP2(line)) {
            p2 += 1
        }
    }

    println(p1) // Part 1
    println(p2) // Part 2
}

fun checkSafetyP1(list: List<Int>): Boolean {
    if (list.size < 2) return true
    val pairs = list.zipWithNext()

    val isIncreasing = pairs.all { (a, b) ->
        b > a && b - a in 1..3
    }

    val isDecreasing = pairs.all { (a, b) ->
        b < a && a - b in 1..3
    }

    return isIncreasing || isDecreasing
}

fun checkSafetyP2(list: List<Int>): Boolean {
    list.forEachIndexed { index, _ ->
        val newlist = list.filterIndexed { i, _ -> i != index }
        if (checkSafetyP1(newlist)) {
            return true
        }
    }
    
    return false
}
