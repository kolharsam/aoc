package org.example

import java.io.File
import kotlin.math.abs

fun day1() {
    val input1 = File("inputs/input1")
    val lines = input1.readLines()

    val leftList = mutableListOf<Int>()
    val rightList = mutableListOf<Int>()

    lines.forEach { line ->
        val sp = line.split("   ")
        val leftNum = Integer.parseInt(sp[0])
        val rightNum = Integer.parseInt(sp[1])
        leftList.add(leftNum)
        rightList.add(rightNum)
    }

    val leftListSorted = leftList.sorted()
    val rightListSorted = rightList.sorted()

    var diff = 0

    leftListSorted.forEachIndexed { index, leftNum ->
        val rightNum = rightListSorted[index]
        diff += abs(rightNum - leftNum)
    }

    println(diff) // part - 1

//    val leftCounts = leftList.groupingBy { it }.eachCount()
    val rightCounts = rightList.groupingBy { it }.eachCount()

    var sim = 0
    for (l in leftList) {
        if (l in rightCounts) {
            sim += (rightCounts[l]?.times(l)!!)
        }
    }

    println(sim) // part - 2
}