package org.example.ui

enum class MessageType {
    MESSAGE,    // Regular text.
    QUESTION,   // Will present a list of options.
    PROMPT,     // Open-ended response.
    ERROR,      // Reporting problems.
}