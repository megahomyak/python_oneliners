(lambda ns: [input("Нажмите Enter, чтобы сгенерировать пароль") or print("".join(ns["random"].choice(ns["string"].ascii_uppercase + ns["string"].digits) for _ in range(15))) for _ in ns["itertools"].repeat(1)])({"itertools": __import__("itertools"), "random": __import__("random"), "string": __import__("string")})
