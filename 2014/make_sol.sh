# Usage:
#     ./make_sol.sh <problem name>

set -o nounset
set -o errexit

mkdir "$1"
cp template.py "$1/$1.py"
touch "$1/test.in"
