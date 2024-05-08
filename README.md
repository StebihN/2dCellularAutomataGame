![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# 2D Cellular Automata Game

A 2D game where a player can spawn different materials on a map.

The map is a grid of cells that have a certain state. The state represents a type of the material. Each material has its own set of rules on how to act in the environment. The action for every cell in the grid is decided based on its state (type of material) and its surroundings. 

At the start of the game, the grid consists only of air and wall cells that are randomly distributed on the grid. The player can then spawn other materials on the grid by using the keyboard to select a material and spawining it by clicking on the grid with the mouse.

### About cellular Automata

A cellular automaton (cellular automata plural, or CA for short) is a model of a system of cell objects with the following characteristics:

 - The cells live on a grid. (I’ll include examples in both one and two dimensions in this chapter, though a CA can exist in any finite number of dimensions.)
 - Each cell has a state, though a cell’s state can vary over time. The number of possible states is typically finite. The simplest example has the two possibilities of 1 and 0 (otherwise referred to as on and off, or alive and dead).
 - Each cell has a neighborhood. This can be defined in any number of ways, but it’s typically all the cells adjacent to that cell.

[More about Cellular automata](https://natureofcode.com/cellular-automata/#what-is-a-cellular-automaton)

### Materials
####  1. Sand
Sand will continue to fall down as long as there is and `air` cell type underneath it. If there isn't, it will check for `air` cells at the bottom left and bottom right corners and randomly move to one. This results to a pile being formed.

![Sand](https://github.com/StebihN/2dCellularAutomataGame/assets/121977112/af0d56b9-1f2b-41b8-8313-2892c58b30e4)

#### 2. Smoke
Smoke is made when a `fire` cell type touches the ground or if a `wood` cell type has a `fire` cell type in its surroundings. Smoke will travel in a random upwards direction and will be present on the map for 20 cycles and then disappear. Smoke is a darker colour if it was made as a result of burning `wood` cell types.

![Smoke](https://github.com/StebihN/2dCellularAutomataGame/assets/121977112/49142c74-7a21-40dc-b03a-a4f887a063a4)

#### 3. Fire
Fire will travel randomly to the bottom until it touches anything that is not an `air` cell type. It will then turn to smoke. It also turns `wood` cell types to dark smoke if it is in its surroundings.

![Fire](https://github.com/StebihN/2dCellularAutomataGame/assets/121977112/2868730e-ed17-4b46-b4b7-ad5512987b7b)

#### 4. Balloon
A Balloon will travel straight up until it touches the ceiling and pops.

![Balloon](https://github.com/StebihN/2dCellularAutomataGame/assets/121977112/a00d3e2c-17cf-4302-9ec8-c080f501fd90)

#### 5. Wall
A Wall is a cell type that gets randomly distributed on the map when the game starts. By default, it cannot be spawned.

![Wall](https://github.com/StebihN/2dCellularAutomataGame/assets/121977112/61977ec6-43eb-4206-9100-7fbb75ac0550)

#### 6. Water
Water is the most complex cell type in the game. It will check for `air` cell types in its surroundings and then spread. The amount of water that spreads around is decided based on its mass. The more mass a `water` cell type has, the darker color it is. If a `sand` cell type touches the `water` cell type, it will sink to the bottom. If a `wood` cell type touches it, it will float. 

![Water](https://github.com/StebihN/2dCellularAutomataGame/assets/121977112/134b7c45-72f4-4165-b156-0f33ff058a36)

#### 7. Wood
Wood falls straight down until it reaches the floor. If a `fire` cell type is in its surroundings, it will turn to a dark `smoke` cell type.

![Wood](https://github.com/StebihN/2dCellularAutomataGame/assets/121977112/b642d34a-e33d-456a-bd88-c49bcbfd5f6b)

### Game controls

| Control               | Action                       |
| :-------------------- | :--------------------------- |
| `a`                   |  Set material to Sand        |
| `s `                  |  Set material to Fire        |
| `d `                  |  Set material to Wood        |
| `f `                  |  Set material to Water       |
| `g `                  |  Set material to Balloon     |
| `left mouse button `  |  Spawn the selected material |

## Motivation

The motivation for this project was to learn about cellular automata and explore possible uses for it.


## Creating New Materials

This code is designed to facilitate the creation of new materials. Follow the steps below to add a new material:

### 1. Create a New Material File

Navigate to the `Materials.Usable` directory and create a new file for your material.

### 2. Define the Material Class

In the newly created file, define a class that inherits from the `Materials.Cell` class. This class should have two properties:

| Property    | Description                              |
|-------------|----------------------------------------- |
| `cell_type` | Specify the type (material) of the cell. |
| `color`     | Set the color of the material.           |

Example:
```python
class NewMaterial(Cell):
    def __init__(self, cell_type, color):
        super().__init__(cell_type, color)
        # add unique properties if needed
```

### 3. Implement the Update Method
Inside your material class, implement the update method. This method should take in the surroundings of the cell and decide its state for the next frame. The update method should return two values:


| Return    | Description                                               | Possible values                                                                                                                                                |
|-----------|---------------------------------------------------------- |--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First     | The material in the current cell for the next frame       | - `None` if the material remains the same<br>- Any other material                                                                                              |
| Second    | The direction in which the current material needs to move | - `None` if the material doesn't move <br>-`top_left`<br>- `top`<br>- `top_right`<br>- `left`<br>- `right`<br>- `bottom_left`<br>- `bottom`<br>- `bottom_right`|

Example:
```python
def update(self, surroundings):
    # Logic to determine the next state of the cell and movement direction

    return new_material, movement_direction
```
