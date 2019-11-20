# Docker Introduction

## Why containers?
Address compatability issues

## Architecture
<pre>
|---------|   |---------|          |---------|   |---------|    
|software1|   |software2|          |software2|   |software4|
|---------|   |---------|          |---------|   |---------|

|----------------------------------------------------------|
|                        Docker                            |
|----------------------------------------------------------|

|----------------------------------------------------------|
|                       OS Kernal                          |
|----------------------------------------------------------|
</pre>
Each software can run in their own environment (with libraries and dependencies) as long as the environment is a distribution based on the OS kernal.

## Containers v.s. Image
An image is a package (or template) used to create containers.
