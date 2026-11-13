package org.example.coffee

import org.example.ui.MessageType
import org.example.ui.UIOption

class CoffeeViewCLI(
    private val viewModel: CoffeeViewModel,
) {
    // Consume UI state, render it, and return user input.
    fun run() {
        while (true) {
            val state = viewModel.state.value
            render(state)
            break
        }
    }

    fun render(state: CoffeeState) {
        println(state.title)
        for (message in state.messages) {
            val type = when (message.type) {
                MessageType.ERROR -> "ERROR"
                MessageType.MESSAGE -> "MESSAGE"
                MessageType.QUESTION -> "QUESTION"
                MessageType.PROMPT -> "PROMPT"
            }
            println("${message.text} ($type)")
        }
        for (option in state.options) {
            println("- ${option.label}")
        }
    }
}