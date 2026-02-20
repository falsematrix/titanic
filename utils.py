def fillna_with_mean(df, cols):
    df[cols] = df[cols].fillna(value=df[cols].mean())
    return df


def sleep(h):
    import time 
    time.sleep(h * 3600)