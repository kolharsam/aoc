package org.example

import java.io.File

fun day9() {
    val input = File("inputs/input9-example").readLines().first().split("")
    val fb_p1 = mutableListOf<String>()

    var st = 0
    var dot = false
    input.forEach { num ->
        if (!(num.isEmpty() || num.isBlank())) {
            if (!dot) {
                fb_p1.add()
            }
        }
    }
}