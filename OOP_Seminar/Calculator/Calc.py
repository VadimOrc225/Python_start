# Модель (Model) - отвечает за логику вычислений
from CalculatorModel import CalculatorModel
from CalculatorPresenter import CalculatorPresenter
from CalculatorView import CalculatorView

# Создание объектов модели, представления и презентера
model = CalculatorModel()
view = CalculatorView()
presenter = CalculatorPresenter(model, view)

# Вызов метода для выполнения вычислений
presenter.calculate()

