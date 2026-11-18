// =========================================================
// Проверка полей формы прямо в браузере (Этап 5 и Этап 8)
// Правила валидации соответствуют заданию демонстрационного экзамена
// =========================================================

const rules = {
    login: {
        test: (v) => /^[A-Za-z0-9]{6,}$/.test(v),
        message: "Только латиница и цифры, не менее 6 символов",
    },
    password: {
        test: (v) => v.length >= 8,
        message: "Пароль должен быть не короче 8 символов",
    },
    full_name: {
        test: (v) => /^[А-Яа-яЁё ]+$/.test(v),
        message: "Только кириллица и пробелы",
    },
    phone: {
        test: (v) => /^8\(\d{3}\)\d{3}-\d{2}-\d{2}$/.test(v),
        message: "Формат: 8(XXX)XXX-XX-XX",
    },
    email: {
        test: (v) => /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v),
        message: "Формат: name@example.ru",
    },
};

// Показать или убрать ошибку под полем
function showError(input, text) {
    let errorBox = null;
    const parent = input.parentElement;
    if (parent) {
        errorBox = parent.querySelector(".form__error");
    }
    if (!errorBox) {
        errorBox = document.querySelector(`.form__error[data-for="${input.name}"]`);
    }
    if (errorBox) {
        errorBox.textContent = text;
    }
    input.classList.toggle("is-invalid", text !== "");
}

// Проверить одно поле. Вернуть true, если поле заполнено верно
function checkField(input, useRules) {
    const value = input.value.trim();
    if (value === "") {
        showError(input, "Поле обязательно для заполнения");
        return false;
    }
    const rule = rules[input.name];
    if (useRules && rule && !rule.test(value)) {
        showError(input, rule.message);
        return false;
    }
    showError(input, "");
    return true;
}

// На странице регистрации проверяем формат, на странице входа — только заполненность
const registerForm = document.querySelector("#registerForm");
const loginForm = document.querySelector("#loginForm");
const currentForm = registerForm || loginForm;
const useRules = Boolean(registerForm && currentForm === registerForm);

if (currentForm) {
    const inputs = currentForm.querySelectorAll("input:not([type='hidden']):not([type='submit']):not([type='radio'])");

    // Проверка при уходе с поля (событие blur)
    inputs.forEach((input) => {
        input.addEventListener("blur", () => checkField(input, useRules));
        input.addEventListener("input", () => {
            if (input.classList.contains("is-invalid")) {
                checkField(input, useRules);
            }
        });
    });

    // Проверка всех полей перед отправкой (событие submit)
    currentForm.addEventListener("submit", (event) => {
        let allValid = true;
        inputs.forEach((input) => {
            if (!checkField(input, useRules)) {
                allValid = false;
            }
        });
        if (!allValid) {
            event.preventDefault(); // отменяем отправку формы с ошибками
        }
    });
}
