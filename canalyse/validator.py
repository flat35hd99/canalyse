class ConductivityValidator:
    def __init__(self, df) -> None:
        self.df = df

    def deviation_is_less_than(self, threshold):
        deviation = self.df["conductivity"].std()
        return deviation < threshold

    def deviation_is_more_than(self, threshold):
        deviation = self.df["conductivity"].std()
        return deviation > threshold
