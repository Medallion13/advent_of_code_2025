# Advent of Code 2025 - Medallion Solutions

Mi repositorio de soluciones para [Advent of Code 2025](https://adventofcode.com/2025).

## 📋 Requisitos Previos

- Python 3.12+
- [Poetry](https://python-poetry.org/) 2.0+
- Make (opcional pero recomendado)

## 🚀 Instalación
```bash
# Clonar el repositorio
git clone https://github.com/Medallion13/advent_of_code_2025.git
cd advent_of_code_2025

# Instalar dependencias
poetry install

# Verificar instalación
make check
```

## 📁 Estructura del Proyecto
```
advent_of_code_2025/
├── pyproject.toml          # Configuración de Poetry y herramientas
├── poetry.lock             # Dependencias exactas (commiteado)
├── Makefile                # Comandos de automatización
├── README.md               # Este archivo
├── CONTRIBUTING.md         # Guía de contribución y workflow Git
├── day1/                   # Solución del día 1
│   ├── __init__.py
│   ├── solution.py         # Código de la solución
│   └── tests/
│       ├── __init__.py
│       └── test_day1.py    # Tests unitarios
├── day2/                   # Solución del día 2
│   └── ...
└── ...
```

## 🛠️ Comandos Disponibles

### Comandos principales:
```bash
make install     # Instalar dependencias
make test        # Ejecutar todos los tests con coverage
make test-fast   # Ejecutar tests sin coverage (más rápido)
make lint        # Verificar linting (Ruff)
make format      # Formatear código automáticamente
make typecheck   # Verificar tipos (Mypy)
make check       # Ejecutar todas las verificaciones (pre-commit)
make clean       # Limpiar archivos de cache
```

### Comandos de Poetry:
```bash
# Ejecutar tests de un día específico
poetry run pytest day1/tests/ -v

# Ejecutar script de un día
poetry run python day1/solution.py
```

## 📝 Workflow de Desarrollo

### Agregar un nuevo día:
```bash
# Crear estructura para el nuevo día
mkdir -p dayN/tests
touch dayN/__init__.py
touch dayN/solution.py
touch dayN/tests/__init__.py
touch dayN/tests/test_solution.py
```

### Template de solution.py:
```python
"""Solution for Advent of Code 2025 - Day N."""


def solve_part1(data: str) -> int:
    """Solve part 1."""
    # Tu código aquí
    return 0


def solve_part2(data: str) -> int:
    """Solve part 2."""
    # Tu código aquí
    return 0


if __name__ == "__main__":
    # Test con input de ejemplo
    sample_input = """
    ejemplo aquí
    """
    print(f"Part 1: {solve_part1(sample_input)}")
    print(f"Part 2: {solve_part2(sample_input)}")
```

### Template de test_solution.py:
```python
"""Tests for day N solutions."""
import pytest

from dayN.solution import solve_part1, solve_part2


@pytest.mark.unit
def test_solve_part1_example():
    """Test part 1 with example input."""
    input_data = "ejemplo"
    assert solve_part1(input_data) == expected_result


@pytest.mark.unit
def test_solve_part2_example():
    """Test part 2 with example input."""
    input_data = "ejemplo"
    assert solve_part2(input_data) == expected_result
```

### Ciclo de desarrollo:
```bash
# 1. Escribir código
code dayN/solution.py

# 2. Escribir tests
code dayN/tests/test_solution.py

# 3. Ejecutar tests mientras desarrollas
make test

# 4. Antes de commit
make check

# 5. Commit
git add dayN/
git commit -m "feat(dayN): solve part 1 and 2"
```

## 🧪 Testing

### Ejecutar tests:
```bash
# Todos los tests con coverage
make test

# Tests sin coverage (rápido)
make test-fast

# Tests de un día específico
poetry run pytest day1/tests/ -v

# Tests con markers
poetry run pytest -m unit          # Solo tests unitarios
poetry run pytest -m "not slow"    # Excluir tests lentos
```

### Ver reporte de coverage:
```bash
# En terminal
make test

# En navegador (HTML)
open htmlcov/index.html  # Mac
xdg-open htmlcov/index.html  # Linux
```

## 🔧 Herramientas Configuradas

| Herramienta | Propósito | Configuración |
|-------------|-----------|---------------|
| **Poetry** | Gestión de dependencias | `pyproject.toml` |
| **Ruff** | Linting y formatting | `pyproject.toml` |
| **Pytest** | Testing y coverage | `pyproject.toml` |
| **Mypy** | Type checking | `pyproject.toml` |
| **Make** | Automatización | `Makefile` |

### Reglas de linting activas:

- `E`: pycodestyle errors
- `F`: Pyflakes (variables sin usar, imports incorrectos)
- `I`: isort (ordenamiento de imports)
- `UP`: pyupgrade (sintaxis moderna de Python)
- `B`: flake8-bugbear (bugs comunes)
- `N`: pep8-naming (convenciones de nombres)

### Type checking:

- Modo estricto (`strict = true`)
- Todos los tipos deben estar declarados
- Tests tienen reglas más relajadas


## 📊 Progreso

| Día | Parte 1 | Parte 2 | Notas |
|-----|---------|---------|-------|
| 1   | ⏳      | ⏳      | - |
| 2   | ⏳      | ⏳      | - |
| ... | ...     | ...     | ... |

## 📚 Recursos

- [Advent of Code 2025](https://adventofcode.com/2025)
- [Python 3.12 Documentation](https://docs.python.org/3.12/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Pytest Documentation](https://docs.pytest.org/)

## 📄 Licencia

Este proyecto es de uso personal para aprendizaje.

---

⭐ **Advent of Code** es creado por [Eric Wastl](http://was.tl/)

---
> readme generado usado Claude.ai
