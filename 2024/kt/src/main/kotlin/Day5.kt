package org.example

import java.io.File

fun day5() {
    val input = File("inputs/input5").readLines()
    val orders = mutableSetOf<Pair<Int, Int>>()
    val pages = mutableListOf<List<Int>>()

    // Parse input
    input.forEach { line ->
        when {
            line.contains("|") -> {
                val (a, b) = line.split("|")
                orders.add(Pair(a.toInt(), b.toInt()))
            }
            line.contains(",") -> {
                pages.add(line.split(",").map { it.toInt() })
            }
        }
    }

    val rightOrders = pages.filter { page ->
        page.indices.all { index ->
            val current = page[index]
            val rest = page.subList(index + 1, page.size)
            rest.all { next ->
                orders.contains(Pair(current, next))
            }
        }
    }

    val wrongOrders = pages.filter { page -> !rightOrders.contains(page) }

    val mids = rightOrders.mapNotNull { it.middle() }
    println(mids.sum()) // This is Part 1

    val newRightOrders = mutableListOf<List<Int>>()

    wrongOrders.forEach { ord ->
        val perms = ord.lazyPermutations()
        for (p in perms) {
            if (p.indices.all { index ->
                    val current = p[index]
                    val rest = p.subList(index + 1, p.size)
                    rest.all { next ->
                        orders.contains(Pair(current, next))
                    }
                }) {
                newRightOrders.add(p)
                break
            }
        }
    }

    val mids2 = newRightOrders.mapNotNull { it.middle() }
    println(mids2.sum()) // This is for part 2
}

fun <T> List<T>.middle(): T? {
    return if (this.isNotEmpty()) this[this.size / 2] else null
}

fun <T : Number> List<T>.sum(): Int {
    return this.fold(0) { acc, num -> acc + num.toInt() }
}

fun <T> List<T>.lazyPermutations(): Sequence<List<T>> = sequence {
    if (this@lazyPermutations.size == 1) {
        yield(this@lazyPermutations)
    } else {
        for (i in this@lazyPermutations.indices) {
            val element = this@lazyPermutations[i]
            val remaining = this@lazyPermutations.filterIndexed { index, _ -> index != i }
            for (perm in remaining.lazyPermutations()) {
                yield(listOf(element) + perm)
            }
        }
    }
}

