class WeightLimitExceededError(Exception):

    
    def __init__(self, limit: int, current: int):
        #we are calling super class. This is right way.
        super.__init__(f"Weight limit exceeded: Limit={limit}, Current={current}")
        self.limit = limit
        self.current = current


class WeightNegativeError(Exception):

    def __init__(self, weight: int):
        #Here we are not calling super class. This may cause some issue at run time. But code will clean.
        self.weight = weight
        self.message = f"Weight cannot be negative: Weight = {weight}"


class Container:
    def __init__(self, limit: int):
        self.limit = limit
        self.current_weight = 0

    def load_item(self, weight: int):
        if weight < 0:
            raise WeightNegativeError(weight)

        new_weight = weight + self.current_weight

        if new_weight > self.limit:
            raise WeightLimitExceededError(self.limit, new_weight)

        self.current_weight = new_weight
        print("Item Loaded")


def main() -> None:
    try:
        container = Container(limit=100)
        container.load_item(50)  # This should work fine
        container.load_item(-60)  # This will raise a WeightLimitExceededError
    except WeightLimitExceededError as e:
        print(e)
    except WeightNegativeError as e:
        print(e.message)


if __name__ == "__main__":
    main()
