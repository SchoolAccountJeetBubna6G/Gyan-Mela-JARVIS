def test_threading():
    from multiprocessing import Pool
    from multiprocessing.dummy import Pool as ThreadPool

    pool = ThreadPool(2)
