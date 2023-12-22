import sys
from collections import deque
from math import lcm
import helper

lines, _, _ = helper.read(sys.argv[1], lines=True)

# Modules name: (name, code, state, el)
M = {}

## Parsing
for line in lines:
	name, l = line.split(" -> ")
	el = l.split(", ")

	if line.startswith("broadcaster"):
		M[name] = (name, 0, None, el)
	else:
		code = 1
		state = False

		if name[0] == '&':
			code = 2
			state = {}

		M[name[1:]] = (name[1:], code, state, el)

## Update connections for conjunction and locate the one who send to rx
imp = ""
for inp, _, _, el in M.values():
	for name in el:
		if name not in M:
			continue
		_, code, state, _ = M[name]

		if code == 2: # Conjunction
			state[inp] = False

	# Which one send to rx ?
	if "rx" in el:
		imp = inp

# Store which modules send to the conjunction module that send to rx
watch = []
for inp, _, _, el in M.values():
	if 'th' in el:
		watch.append(inp)

def broadcaster(module, pulse, out):
	_, sig = pulse
	inp, _, _, el = module

	for dst in el:
		out.append((inp, dst, sig))

def flipflop(module, pulse, out):
	_, sig = pulse
	if sig: # High does nothing
		return

	inp, code, state, el = module

	# Switch state and register new state
	state = not state
	M[inp] = (inp, code, state, el)

	for dst in el:
		out.append((inp, dst, state))

def conjunction(module, pulse, out):
	inp, sig = pulse
	inp1, code, state, el = module

	outp = True
	state[inp] = sig

	if all(state.values()):
		outp = False

	for dst in el:
		out.append((inp1, dst, outp))

events = [0,0]
part2 = 1
pulses = deque()
for i in range(1000000):
	pulses.append(("button", "broadcaster", False))

	while pulses:
		inp, dst, sig  = pulses.popleft()

		events[sig] += 1

		if dst not in M:
			continue

		if inp in watch and sig:
			part2 = lcm(part2, i + 1)
			watch.remove(inp)

			if len(watch) == 0:
				print("Part2:", part2)
				exit()

		pulse = (inp, sig)
		module = M[dst]
		_, code, _, _ = module

		if code == 0:
			broadcaster(module, pulse, pulses)
		elif code == 1:
			flipflop(module, pulse, pulses)
		else:
			conjunction(module, pulse, pulses)

	if i == 1000 - 1:
		print("Part1:", helper.prod(events))