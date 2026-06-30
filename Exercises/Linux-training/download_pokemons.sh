#!/bin/bash

for pokemon in $(cat data/pokemons/pokemon_list.txt)
do
    curl https://pokeapi.co/api/v2/pokemon-species/$pokemon > data/pokemons/$pokemon.json
    sleep 2
done
