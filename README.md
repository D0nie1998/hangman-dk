# HANGMAN

## Table of Contents

1. [**Introduction**](#introduction)

2. [**User Experience(UX)**](#user-experience(ux))
     
3. [**Features**](features)
     
4. [**Technology Used**](#technology-used)
    - [**Languages Used**](#languages-used)
    - [**Frameworks**](#frameworks,-libraries-&-programs-used)
 
5. [**Testing**](#testing)
      - [**Validation**](#validation)
      - [**Issues**](#issues)
6. [**Deployment**](#deployment)
      - [**Heroku**](#heroku)
7. [**Credits**](#credits)

# Introduction

</br>
</br>

For my third portfolio project, I have chosen the popular and enjoyable game known as Hangman. I have implemented Hangman as a Python terminal game, which can be accessed through the Code Institute terminal on Heroku.

Upon launching the game, users will be greeted by a welcoming screen and presented with three options. The first option initiates the game, prompting the user to enter a username. After entering a username, the user will be shown an initial stage of the hangman image, which progressively changes with each incorrect guess. Additionally, a randomly selected word will be displayed with underscores representing each letter. As the user correctly guesses letters, they will be revealed in place of the underscores, until either the entire word is guessed correctly or the user exhausts their allotted guesses. When the user runs out of lives, the final stage of the hangman will be displayed, depicting a stickman hanging from a platform. At this point, the user will have the choice to play again or save their username and score to Google Sheets.