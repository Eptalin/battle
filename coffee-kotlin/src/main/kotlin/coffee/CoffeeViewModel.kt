package org.example.coffee

import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import org.example.coffee.model.CoffeeType
import org.example.coffee.model.MilkType
import org.example.ui.MessageType
import org.example.ui.UIMessage
import org.example.ui.UIOption

class CoffeeViewModel {

    // Initial UI State
    private val _state = MutableStateFlow(
        CoffeeState(
            title = "Coffee Machine",
            messages = listOf(
                UIMessage("How do you take your coffee?", MessageType.QUESTION),
            ),
            options = listOf(
                UIOption("Black", CoffeeType.BLACK),
                UIOption("White", CoffeeType.WHITE),
            )
        )
    )

    // Expose state to consumers
    val state: StateFlow<CoffeeState> = _state.asStateFlow()

    // Info to create coffee
    private var coffeeType: CoffeeType? = null
    private var milkType = MilkType.NONE
    private var sugars = 0



}