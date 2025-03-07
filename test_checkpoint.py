
from sevenn.calculator import SevenNetCalculator
from ase.build import bulk

atoms = bulk('Mo', 'bcc')
calc = SevenNetCalculator('checkpoint.pth')
atoms.calc = calc

print("energy: ", atoms.get_potential_energy())
print("forces: ", atoms.get_forces())
print("stress: ", atoms.get_stress())