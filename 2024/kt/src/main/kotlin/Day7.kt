package org.example

import java.io.File
import java.math.BigInteger

fun day7() {
    val input = File("inputs/input7").readLines()
    val prods = mutableListOf<Pair<BigInteger, List<BigInteger>>>()

    input.forEach { line ->
        val lsp = line.split(": ")
        val mn = lsp[0].toBigInteger()
        val nms = lsp[1].split(" ").map { s -> s.toBigInteger() }
        prods.add(Pair(mn, nms))
    }

    var c: BigInteger = BigInteger.ZERO

    for ((target, nums) in prods) {
        if (canReachTarget(nums, target)) {
            c += target
        }
    }

    println(c)
}

fun canReachTarget(numbers: List<BigInteger>, target: BigInteger): Boolean {
    fun evaluateLeftToRight(values: List<BigInteger>, operators: List<Char>): BigInteger {
        var result = values[0]
        for (i in operators.indices) {
            result = when (operators[i]) {
                '+' -> result + values[i + 1]
                '*' -> result * values[i + 1]
                '|' -> (result.toString() + values[i+1].toString()).toBigInteger()
                else -> throw IllegalArgumentException("Unsupported operator")
            }
        }
        return result
    }

    fun backtrack(index: Int, operators: MutableList<Char>): Boolean {
        // If we have placed operators between all numbers, evaluate the result
        if (index == numbers.size - 1) {
            return evaluateLeftToRight(numbers, operators) == target
        }

        // Try both '+' and '*' at the current position
        operators.add('+')
        if (backtrack(index + 1, operators)) return true
        operators.removeAt(operators.size - 1)

        operators.add('*')
        if (backtrack(index + 1, operators)) return true
        operators.removeAt(operators.size - 1)

        operators.add('|')
        if (backtrack(index + 1, operators)) return true
        operators.removeAt(operators.size - 1)

        return false
    }

    return backtrack(0, mutableListOf())
}
