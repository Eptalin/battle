package org.example

import org.example.coffee.CoffeeViewCLI
import org.example.coffee.CoffeeViewModel

fun main() {
    val cli = CoffeeViewCLI(CoffeeViewModel())
    cli.run()
}
