# fib5.py
# Aus "Algorithmen in Python", Kapitel 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
def fib5(n: int) -> int:
    if n == 0: return n  # Spezialfall
    last: int = 0  # Am Anfang auf fib(0) setzen
    next: int = 1  # Am Anfang auf fib(1) setzen
    for _ in range(1, n):
        last, next = next, last + next
    return next


if __name__ == "__main__":
    print(fib5(2))
    print(fib5(50))

