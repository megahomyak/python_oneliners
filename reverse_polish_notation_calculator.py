(lambda reduce: (
    lambda number_regex_pattern, stack, roll_iterable: roll_iterable(
        (
            roll_iterable(
                (
                    print(
                        f'Unknown word "{minimal_stack_size}" (word number is '
                        f'{word_number})! Skipping it.'
                    )
                    if number_regex_pattern.fullmatch(
                        minimal_stack_size
                    ) is None else
                    stack.append(int(minimal_stack_size))
                )
                if operation is None else
                (
                    print(
                        f"Not enough elements on stack to perform "
                        f"{operation_name} (word number {word_number})! ("
                        f"Required: {minimal_stack_size}, stack length: "
                        f"{len(stack)})"
                    )
                    if len(stack) < minimal_stack_size else
                    stack.append(operation(stack))
                )
                for word_number, (
                    minimal_stack_size, operation, operation_name
                ) in enumerate(
                    (
                        {
                            "+": (
                                2, lambda stack: stack.pop() + stack.pop(),
                                "addition"
                            ),
                            "-": (2, lambda stack: (
                                lambda stack, right_operand: (
                                    stack.pop() - right_operand
                                )
                            )(stack, stack.pop()), "subtraction"),
                            "*": (
                                2, lambda stack: stack.pop() * stack.pop(),
                                "multiplication"
                            ),
                            "/": (2, lambda stack: (
                                lambda stack, right_operand: (
                                    stack.pop() / right_operand
                                )
                            )(stack, stack.pop()), "division"),
                            "abs": (
                                1, lambda stack: abs(stack.pop()), "modulus"
                            )
                        }.get(word, (word, None, None))
                        for word in input().split()
                    ),
                    start=1
                )
            ) == (
                print("Stack is empty, nothing to print")
                if len(stack) == 0 else
                (
                    print("Stack (from bottom to top):", ", ".join(
                        map(str, stack)
                    )) == stack.clear()
                )
            )
        ) for _ in __import__("itertools").repeat(1)
    )
)(
    __import__("re").compile(r"\d+"),
    [],
    lambda iterable: reduce(lambda _, __: None, iterable)
))(
    __import__("functools").reduce
)
