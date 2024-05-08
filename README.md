# 2D Cellular Automata Game
This project is a 2D Cellular Automata game. A random map is created upon starting the game. The player can then spawn in different materials that each have their own logic on how to act in the environment. The action is decided based on the surroundings of the current cell and its type. 
## Materials 

### Sand
Sand will continue to fall down as long as there is and `air` cell type underneath it. If there isn't, it will check for `air` cells at the bottom left and bottom right corners and randomly move to one. This results to a pile being formed.

### Smoke
Smoke is made when a `fire` cell type touches the ground or if a `wood` cell type has a `fire` cell type in its surroundings. Smoke will travel in a random upwards direction and will be present on the map for 20 cycles and then disappear. Smoke is a darker colour if it was made as a result of burning `wood` cell types.

### Fire
Fire will travel randomly to the bottom until it touches anything that is not an `air` cell type. It will then turn to smoke. It also turns `wood` cell types to dark smoke if it is in its surroundings.

### Balloon
A Balloon will travel straight up until it touches the ceiling and pops.

### Wall
A Wall is a cell type that gets randomly distributed on the map when the game starts. By default, it cannot be spawned.

### Water
Water is the most complex cell type in the game. It will check for `air` cell types in its surroundings and then spread. The amount of water that spreads around is decided based on its mass. The more mass a `water` cell type has, the darker color it is. If a `sand` cell type touches the `water` cell type, it will sink to the bottom. If a `wood` cell type touches it, it will float. 

### Wood
Wood falls straight down until it reaches the floor. If a `fire` cell type is in its surroundings, it will turn to a dark `smoke` cell type.

## Creating new materials:
The code is designed in a way that allows the creation of new materials. To create a new element, create a new file in the `Materials.Usable` directory. Create a class that inherits from the `Materials.Cell` class. It requires a `cell_type` and a `color` property. Create a method called `update` that takes in a cells surroundings. Write the logic that decides what happens with the material in each loop that updates the game state. The method should return `None` and `None` if the current cell should remain the same material and if the current material should not move. If the current cell should become a new material, return the Material. If the current material needs to move, return 
`top_left`, `top`, `top_right`, `left`, `right`, `bottom_left`, `bottom` or `bottom_right`

