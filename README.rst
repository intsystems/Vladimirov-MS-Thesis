|test| |codecov| |docs|

.. |test| image:: https://github.com/intsystems/ProjectTemplate/workflows/test/badge.svg
    :target: https://github.com/intsystems/ProjectTemplate/tree/master
    :alt: Test status
    
.. |codecov| image:: https://img.shields.io/codecov/c/github/intsystems/ProjectTemplate/master
    :target: https://app.codecov.io/gh/intsystems/ProjectTemplate
    :alt: Test coverage
    
.. |docs| image:: https://github.com/intsystems/ProjectTemplate/workflows/docs/badge.svg
    :target: https://intsystems.github.io/ProjectTemplate/
    :alt: Docs status


.. class:: center

    :Название исследуемой задачи: Причинно-ориентированное снижение размерности для анализа данных нейроинтерфейсов
    :Тип научной работы: НИР
    :Автор: Владимиров Эдуард Анатольевич
    :Научный руководитель: д.ф-м.н. Стрижов Вадим Викторович
    :Научный консультант(при наличии): -

Abstract
========

Learning low–dimensional representations that preserve cause–and–effect structure is a key step toward interpretable modelling of high-dimensional dynamical data.
		This thesis introduces \textbf{CaSCA}, a linear auto-encoder that splits the latent space into a causal block, capturing delayed directed influence from one multivariate series to another, and a reconstructive block, keeping residual variance.  
		Extensions to trajectory embeddings, Riemannian covariance spaces, and a deep variant with a differentiable Convergent Cross Mapping loss broaden the framework.  
		Comprehensive experiments on two real-world datasets—dual accelerometer-gyroscope recordings and EEG–IMU traces of table-tennis sessions—show that CaSCA  
		(i) reduces multicollinearity,  
		(ii) reconstructs signals with negligible loss of explained variance, and  
		(iii) improves downstream prediction
		The method thus offers a compact, interpretable state-space where causal links are easier to detect and exploit.

