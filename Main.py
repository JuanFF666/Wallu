from proyecto_wallu import Wallu
from wallu import WalluInterface
from RobotStateMachi import RobotStateMachine

# Crear instancias de los módulos
wallu = Wallu()
interface = WalluInterface()
state_machine = RobotStateMachine()

# Conectar los módulos
wallu.set_interface(interface)
wallu.set_state_machine(state_machine)
interface.set_wallu(wallu)
state_machine.set_wallu(wallu)

# Iniciar el programa
if __name__ == "__main__":
    wallu.start()
