# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 871, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mms = QtWidgets.QWidget()
        self.tab_mms.setObjectName("tab_mms")
        self.input_arrival_rate_mms = QtWidgets.QLineEdit(self.tab_mms)
        self.input_arrival_rate_mms.setGeometry(QtCore.QRect(200, 30, 110, 20))
        self.input_arrival_rate_mms.setObjectName("input_arrival_rate_mms")
        self.input_num_servers_mms = QtWidgets.QLineEdit(self.tab_mms)
        self.input_num_servers_mms.setGeometry(QtCore.QRect(200, 90, 110, 20))
        self.input_num_servers_mms.setObjectName("input_num_servers_mms")
        self.btn_simulate_mms = QtWidgets.QPushButton(self.tab_mms)
        self.btn_simulate_mms.setGeometry(QtCore.QRect(370, 30, 100, 40))
        self.btn_simulate_mms.setObjectName("btn_simulate_mms")
        self.label_service_rate_mms = QtWidgets.QLabel(self.tab_mms)
        self.label_service_rate_mms.setGeometry(QtCore.QRect(20, 60, 140, 20))
        self.label_service_rate_mms.setObjectName("label_service_rate_mms")
        self.btn_clear_mms = QtWidgets.QPushButton(self.tab_mms)
        self.btn_clear_mms.setGeometry(QtCore.QRect(370, 80, 100, 30))
        self.btn_clear_mms.setObjectName("btn_clear_mms")
        self.input_service_rate_mms = QtWidgets.QLineEdit(self.tab_mms)
        self.input_service_rate_mms.setGeometry(QtCore.QRect(200, 60, 110, 20))
        self.input_service_rate_mms.setObjectName("input_service_rate_mms")
        self.label_num_servers_mms = QtWidgets.QLabel(self.tab_mms)
        self.label_num_servers_mms.setGeometry(QtCore.QRect(20, 90, 140, 20))
        self.label_num_servers_mms.setObjectName("label_num_servers_mms")
        self.label_arrival_rate_mms = QtWidgets.QLabel(self.tab_mms)
        self.label_arrival_rate_mms.setGeometry(QtCore.QRect(20, 30, 140, 20))
        self.label_arrival_rate_mms.setObjectName("label_arrival_rate_mms")
        self.progress_bar_mms = QtWidgets.QProgressBar(self.tab_mms)
        self.progress_bar_mms.setGeometry(QtCore.QRect(740, 140, 118, 23))
        self.progress_bar_mms.setProperty("value", 0)
        self.progress_bar_mms.setObjectName("progress_bar_mms")
        self.btn_view_images_mms = QtWidgets.QPushButton(self.tab_mms)
        self.btn_view_images_mms.setGeometry(QtCore.QRect(740, 30, 110, 35))
        self.btn_view_images_mms.setObjectName("btn_view_images_mms")
        self.tabWidget.addTab(self.tab_mms, "")
        self.tab_q_finite_length = QtWidgets.QWidget()
        self.tab_q_finite_length.setObjectName("tab_q_finite_length")
        self.label_service_rate_finite_q_length = QtWidgets.QLabel(self.tab_q_finite_length)
        self.label_service_rate_finite_q_length.setGeometry(QtCore.QRect(20, 60, 140, 20))
        self.label_service_rate_finite_q_length.setObjectName("label_service_rate_finite_q_length")
        self.label_num_servers_finite_q_length = QtWidgets.QLabel(self.tab_q_finite_length)
        self.label_num_servers_finite_q_length.setGeometry(QtCore.QRect(20, 90, 140, 20))
        self.label_num_servers_finite_q_length.setObjectName("label_num_servers_finite_q_length")
        self.progress_bar_finite_q_length = QtWidgets.QProgressBar(self.tab_q_finite_length)
        self.progress_bar_finite_q_length.setGeometry(QtCore.QRect(740, 140, 118, 23))
        self.progress_bar_finite_q_length.setProperty("value", 0)
        self.progress_bar_finite_q_length.setObjectName("progress_bar_finite_q_length")
        self.btn_simulate_finite_q_length = QtWidgets.QPushButton(self.tab_q_finite_length)
        self.btn_simulate_finite_q_length.setGeometry(QtCore.QRect(370, 30, 100, 40))
        self.btn_simulate_finite_q_length.setObjectName("btn_simulate_finite_q_length")
        self.input_arrival_rate_finite_q_length = QtWidgets.QLineEdit(self.tab_q_finite_length)
        self.input_arrival_rate_finite_q_length.setGeometry(QtCore.QRect(200, 30, 110, 20))
        self.input_arrival_rate_finite_q_length.setObjectName("input_arrival_rate_finite_q_length")
        self.input_service_rate_finite_q_length = QtWidgets.QLineEdit(self.tab_q_finite_length)
        self.input_service_rate_finite_q_length.setGeometry(QtCore.QRect(200, 60, 110, 20))
        self.input_service_rate_finite_q_length.setObjectName("input_service_rate_finite_q_length")
        self.btn_clear_finite_q_length = QtWidgets.QPushButton(self.tab_q_finite_length)
        self.btn_clear_finite_q_length.setGeometry(QtCore.QRect(370, 80, 100, 30))
        self.btn_clear_finite_q_length.setObjectName("btn_clear_finite_q_length")
        self.label_arrival_rate_finite_q_length = QtWidgets.QLabel(self.tab_q_finite_length)
        self.label_arrival_rate_finite_q_length.setGeometry(QtCore.QRect(20, 30, 140, 20))
        self.label_arrival_rate_finite_q_length.setObjectName("label_arrival_rate_finite_q_length")
        self.input_num_servers_finite_q_length = QtWidgets.QLineEdit(self.tab_q_finite_length)
        self.input_num_servers_finite_q_length.setGeometry(QtCore.QRect(200, 90, 110, 20))
        self.input_num_servers_finite_q_length.setObjectName("input_num_servers_finite_q_length")
        self.label_max_queue_length__finite_q_length = QtWidgets.QLabel(self.tab_q_finite_length)
        self.label_max_queue_length__finite_q_length.setGeometry(QtCore.QRect(20, 120, 171, 20))
        self.label_max_queue_length__finite_q_length.setObjectName("label_max_queue_length__finite_q_length")
        self.input_max_queue_length_finite_q_length = QtWidgets.QLineEdit(self.tab_q_finite_length)
        self.input_max_queue_length_finite_q_length.setGeometry(QtCore.QRect(200, 120, 110, 20))
        self.input_max_queue_length_finite_q_length.setObjectName("input_max_queue_length_finite_q_length")
        self.btn_view_images_finite_q_length = QtWidgets.QPushButton(self.tab_q_finite_length)
        self.btn_view_images_finite_q_length.setGeometry(QtCore.QRect(740, 30, 110, 35))
        self.btn_view_images_finite_q_length.setObjectName("btn_view_images_finite_q_length")
        self.tabWidget.addTab(self.tab_q_finite_length, "")
        self.tab_population_finite = QtWidgets.QWidget()
        self.tab_population_finite.setObjectName("tab_population_finite")
        self.label_population_size_finite_population = QtWidgets.QLabel(self.tab_population_finite)
        self.label_population_size_finite_population.setGeometry(QtCore.QRect(20, 120, 201, 20))
        self.label_population_size_finite_population.setObjectName("label_population_size_finite_population")
        self.input_num_servers_finite_population = QtWidgets.QLineEdit(self.tab_population_finite)
        self.input_num_servers_finite_population.setGeometry(QtCore.QRect(230, 90, 110, 20))
        self.input_num_servers_finite_population.setObjectName("input_num_servers_finite_population")
        self.input_arrival_rate_finite_population = QtWidgets.QLineEdit(self.tab_population_finite)
        self.input_arrival_rate_finite_population.setGeometry(QtCore.QRect(230, 30, 110, 20))
        self.input_arrival_rate_finite_population.setObjectName("input_arrival_rate_finite_population")
        self.input_service_rate_finite_population = QtWidgets.QLineEdit(self.tab_population_finite)
        self.input_service_rate_finite_population.setGeometry(QtCore.QRect(230, 60, 110, 20))
        self.input_service_rate_finite_population.setObjectName("input_service_rate_finite_population")
        self.btn_clear_finite_population = QtWidgets.QPushButton(self.tab_population_finite)
        self.btn_clear_finite_population.setGeometry(QtCore.QRect(400, 80, 100, 30))
        self.btn_clear_finite_population.setObjectName("btn_clear_finite_population")
        self.label_num_servers_finite_population = QtWidgets.QLabel(self.tab_population_finite)
        self.label_num_servers_finite_population.setGeometry(QtCore.QRect(20, 90, 140, 20))
        self.label_num_servers_finite_population.setObjectName("label_num_servers_finite_population")
        self.label_service_rate_finite_population = QtWidgets.QLabel(self.tab_population_finite)
        self.label_service_rate_finite_population.setGeometry(QtCore.QRect(20, 60, 140, 20))
        self.label_service_rate_finite_population.setObjectName("label_service_rate_finite_population")
        self.label_arrival_rate_finite_population = QtWidgets.QLabel(self.tab_population_finite)
        self.label_arrival_rate_finite_population.setGeometry(QtCore.QRect(20, 30, 140, 20))
        self.label_arrival_rate_finite_population.setObjectName("label_arrival_rate_finite_population")
        self.input_population_size_finite_population = QtWidgets.QLineEdit(self.tab_population_finite)
        self.input_population_size_finite_population.setGeometry(QtCore.QRect(230, 120, 110, 20))
        self.input_population_size_finite_population.setObjectName("input_population_size_finite_population")
        self.btn_simulate_finite_population = QtWidgets.QPushButton(self.tab_population_finite)
        self.btn_simulate_finite_population.setGeometry(QtCore.QRect(400, 30, 100, 40))
        self.btn_simulate_finite_population.setObjectName("btn_simulate_finite_population")
        self.progress_bar_finite_population = QtWidgets.QProgressBar(self.tab_population_finite)
        self.progress_bar_finite_population.setGeometry(QtCore.QRect(740, 140, 118, 23))
        self.progress_bar_finite_population.setProperty("value", 0)
        self.progress_bar_finite_population.setObjectName("progress_bar_finite_population")
        self.btn_view_images_finite_population = QtWidgets.QPushButton(self.tab_population_finite)
        self.btn_view_images_finite_population.setGeometry(QtCore.QRect(740, 30, 110, 35))
        self.btn_view_images_finite_population.setObjectName("btn_view_images_finite_population")
        self.tabWidget.addTab(self.tab_population_finite, "")
        self.tab_mg1 = QtWidgets.QWidget()
        self.tab_mg1.setObjectName("tab_mg1")
        self.btn_simulate_mg1 = QtWidgets.QPushButton(self.tab_mg1)
        self.btn_simulate_mg1.setGeometry(QtCore.QRect(410, 30, 100, 40))
        self.btn_simulate_mg1.setObjectName("btn_simulate_mg1")
        self.label_average_service_time_mg1 = QtWidgets.QLabel(self.tab_mg1)
        self.label_average_service_time_mg1.setGeometry(QtCore.QRect(20, 60, 180, 20))
        self.label_average_service_time_mg1.setObjectName("label_average_service_time_mg1")
        self.input_standard_dev_mg1 = QtWidgets.QLineEdit(self.tab_mg1)
        self.input_standard_dev_mg1.setGeometry(QtCore.QRect(280, 90, 110, 20))
        self.input_standard_dev_mg1.setObjectName("input_standard_dev_mg1")
        self.label_standard_dev_mg1_2 = QtWidgets.QLabel(self.tab_mg1)
        self.label_standard_dev_mg1_2.setGeometry(QtCore.QRect(20, 90, 240, 20))
        self.label_standard_dev_mg1_2.setObjectName("label_standard_dev_mg1_2")
        self.input_average_service_time_mg1 = QtWidgets.QLineEdit(self.tab_mg1)
        self.input_average_service_time_mg1.setGeometry(QtCore.QRect(280, 60, 110, 20))
        self.input_average_service_time_mg1.setObjectName("input_average_service_time_mg1")
        self.btn_clear_mg1 = QtWidgets.QPushButton(self.tab_mg1)
        self.btn_clear_mg1.setGeometry(QtCore.QRect(410, 80, 100, 30))
        self.btn_clear_mg1.setObjectName("btn_clear_mg1")
        self.input_arrival_rate_mg1 = QtWidgets.QLineEdit(self.tab_mg1)
        self.input_arrival_rate_mg1.setGeometry(QtCore.QRect(280, 30, 110, 20))
        self.input_arrival_rate_mg1.setObjectName("input_arrival_rate_mg1")
        self.label_standard_dev_mg1 = QtWidgets.QLabel(self.tab_mg1)
        self.label_standard_dev_mg1.setGeometry(QtCore.QRect(20, 30, 140, 20))
        self.label_standard_dev_mg1.setObjectName("label_standard_dev_mg1")
        self.progress_bar_mg1 = QtWidgets.QProgressBar(self.tab_mg1)
        self.progress_bar_mg1.setGeometry(QtCore.QRect(740, 140, 118, 23))
        self.progress_bar_mg1.setProperty("value", 0)
        self.progress_bar_mg1.setObjectName("progress_bar_mg1")
        self.tabWidget.addTab(self.tab_mg1, "")
        self.tab_mm1 = QtWidgets.QWidget()
        self.tab_mm1.setObjectName("tab_mm1")
        self.btn_simulate_mm1 = QtWidgets.QPushButton(self.tab_mm1)
        self.btn_simulate_mm1.setGeometry(QtCore.QRect(370, 30, 100, 40))
        self.btn_simulate_mm1.setObjectName("btn_simulate_mm1")
        self.label_service_rate_mm1 = QtWidgets.QLabel(self.tab_mm1)
        self.label_service_rate_mm1.setGeometry(QtCore.QRect(20, 60, 140, 20))
        self.label_service_rate_mm1.setObjectName("label_service_rate_mm1")
        self.input_service_rate_mm1 = QtWidgets.QLineEdit(self.tab_mm1)
        self.input_service_rate_mm1.setGeometry(QtCore.QRect(200, 60, 110, 20))
        self.input_service_rate_mm1.setObjectName("input_service_rate_mm1")
        self.btn_clear_mm1 = QtWidgets.QPushButton(self.tab_mm1)
        self.btn_clear_mm1.setGeometry(QtCore.QRect(370, 80, 100, 30))
        self.btn_clear_mm1.setObjectName("btn_clear_mm1")
        self.input_arrival_rate_mm1 = QtWidgets.QLineEdit(self.tab_mm1)
        self.input_arrival_rate_mm1.setGeometry(QtCore.QRect(200, 30, 110, 20))
        self.input_arrival_rate_mm1.setObjectName("input_arrival_rate_mm1")
        self.label_arrival_rate_mm1 = QtWidgets.QLabel(self.tab_mm1)
        self.label_arrival_rate_mm1.setGeometry(QtCore.QRect(20, 30, 140, 20))
        self.label_arrival_rate_mm1.setObjectName("label_arrival_rate_mm1")
        self.progress_bar_mm1 = QtWidgets.QProgressBar(self.tab_mm1)
        self.progress_bar_mm1.setGeometry(QtCore.QRect(740, 140, 118, 23))
        self.progress_bar_mm1.setProperty("value", 0)
        self.progress_bar_mm1.setObjectName("progress_bar_mm1")
        self.tabWidget.addTab(self.tab_mm1, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.label_settings_round = QtWidgets.QLabel(self.tab_settings)
        self.label_settings_round.setGeometry(QtCore.QRect(20, 30, 111, 18))
        self.label_settings_round.setObjectName("label_settings_round")
        self.input_settings_round = QtWidgets.QLineEdit(self.tab_settings)
        self.input_settings_round.setGeometry(QtCore.QRect(200, 30, 110, 20))
        self.input_settings_round.setObjectName("input_settings_round")
        self.tabWidget.addTab(self.tab_settings, "")
        self.frame_results = QtWidgets.QFrame(self.centralwidget)
        self.frame_results.setEnabled(False)
        self.frame_results.setGeometry(QtCore.QRect(-1, 209, 871, 321))
        self.frame_results.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_results.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_results.setObjectName("frame_results")
        self.list_results = QtWidgets.QListWidget(self.frame_results)
        self.list_results.setGeometry(QtCore.QRect(10, 10, 651, 301))
        self.list_results.setStyleSheet("font-size: 20px;")
        self.list_results.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.list_results.setAutoScroll(True)
        self.list_results.setItemAlignment(QtCore.Qt.AlignLeading)
        self.list_results.setObjectName("list_results")
        self.label_results = QtWidgets.QLabel(self.frame_results)
        self.label_results.setGeometry(QtCore.QRect(670, 20, 191, 281))
        self.label_results.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_results.setObjectName("label_results")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.btn_clear_mms.clicked.connect(self.input_service_rate_mms.clear) # type: ignore
        self.btn_clear_mms.clicked.connect(self.input_arrival_rate_mms.clear) # type: ignore
        self.btn_clear_mms.clicked.connect(self.input_num_servers_mms.clear) # type: ignore
        self.btn_clear_mm1.clicked.connect(self.input_arrival_rate_mm1.clear) # type: ignore
        self.btn_clear_mm1.clicked.connect(self.input_service_rate_mm1.clear) # type: ignore
        self.btn_clear_mm1.clicked.connect(self.progress_bar_mm1.reset) # type: ignore
        self.btn_clear_mms.clicked.connect(self.progress_bar_mms.reset) # type: ignore
        self.btn_clear_finite_q_length.clicked.connect(self.input_arrival_rate_finite_q_length.clear) # type: ignore
        self.btn_clear_finite_q_length.clicked.connect(self.input_service_rate_finite_q_length.clear) # type: ignore
        self.btn_clear_finite_q_length.clicked.connect(self.input_num_servers_finite_q_length.clear) # type: ignore
        self.btn_clear_finite_q_length.clicked.connect(self.input_max_queue_length_finite_q_length.clear) # type: ignore
        self.btn_clear_finite_q_length.clicked.connect(self.progress_bar_finite_q_length.reset) # type: ignore
        self.btn_clear_finite_population.clicked.connect(self.input_arrival_rate_finite_population.clear) # type: ignore
        self.btn_clear_finite_population.clicked.connect(self.input_service_rate_finite_population.clear) # type: ignore
        self.btn_clear_finite_population.clicked.connect(self.input_num_servers_finite_population.clear) # type: ignore
        self.btn_clear_finite_population.clicked.connect(self.input_population_size_finite_population.clear) # type: ignore
        self.btn_clear_finite_population.clicked.connect(self.progress_bar_finite_population.reset) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.input_arrival_rate_mms)
        MainWindow.setTabOrder(self.input_arrival_rate_mms, self.input_service_rate_mms)
        MainWindow.setTabOrder(self.input_service_rate_mms, self.input_num_servers_mms)
        MainWindow.setTabOrder(self.input_num_servers_mms, self.btn_simulate_mms)
        MainWindow.setTabOrder(self.btn_simulate_mms, self.btn_clear_mms)
        MainWindow.setTabOrder(self.btn_clear_mms, self.input_arrival_rate_mm1)
        MainWindow.setTabOrder(self.input_arrival_rate_mm1, self.input_service_rate_mm1)
        MainWindow.setTabOrder(self.input_service_rate_mm1, self.btn_simulate_mm1)
        MainWindow.setTabOrder(self.btn_simulate_mm1, self.btn_clear_mm1)
        MainWindow.setTabOrder(self.btn_clear_mm1, self.input_arrival_rate_mg1)
        MainWindow.setTabOrder(self.input_arrival_rate_mg1, self.input_average_service_time_mg1)
        MainWindow.setTabOrder(self.input_average_service_time_mg1, self.input_standard_dev_mg1)
        MainWindow.setTabOrder(self.input_standard_dev_mg1, self.btn_simulate_mg1)
        MainWindow.setTabOrder(self.btn_simulate_mg1, self.btn_clear_mg1)
        MainWindow.setTabOrder(self.btn_clear_mg1, self.list_results)
        MainWindow.setTabOrder(self.list_results, self.input_arrival_rate_finite_q_length)
        MainWindow.setTabOrder(self.input_arrival_rate_finite_q_length, self.input_service_rate_finite_q_length)
        MainWindow.setTabOrder(self.input_service_rate_finite_q_length, self.input_num_servers_finite_q_length)
        MainWindow.setTabOrder(self.input_num_servers_finite_q_length, self.input_max_queue_length_finite_q_length)
        MainWindow.setTabOrder(self.input_max_queue_length_finite_q_length, self.btn_simulate_finite_q_length)
        MainWindow.setTabOrder(self.btn_simulate_finite_q_length, self.btn_clear_finite_q_length)
        MainWindow.setTabOrder(self.btn_clear_finite_q_length, self.input_arrival_rate_finite_population)
        MainWindow.setTabOrder(self.input_arrival_rate_finite_population, self.input_service_rate_finite_population)
        MainWindow.setTabOrder(self.input_service_rate_finite_population, self.input_num_servers_finite_population)
        MainWindow.setTabOrder(self.input_num_servers_finite_population, self.input_population_size_finite_population)
        MainWindow.setTabOrder(self.input_population_size_finite_population, self.btn_simulate_finite_population)
        MainWindow.setTabOrder(self.btn_simulate_finite_population, self.btn_clear_finite_population)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulador de colas"))
        self.btn_simulate_mms.setText(_translate("MainWindow", "Simular"))
        self.label_service_rate_mms.setText(_translate("MainWindow", "Tasa de servicio:"))
        self.btn_clear_mms.setText(_translate("MainWindow", "Limpiar"))
        self.label_num_servers_mms.setText(_translate("MainWindow", "Número de servidores:"))
        self.label_arrival_rate_mms.setText(_translate("MainWindow", "Tasa de arribos:"))
        self.btn_view_images_mms.setText(_translate("MainWindow", "Ver imágenes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mms), _translate("MainWindow", "M/M/s"))
        self.label_service_rate_finite_q_length.setText(_translate("MainWindow", "Tasa de servicio:"))
        self.label_num_servers_finite_q_length.setText(_translate("MainWindow", "Número de servidores:"))
        self.btn_simulate_finite_q_length.setText(_translate("MainWindow", "Simular"))
        self.btn_clear_finite_q_length.setText(_translate("MainWindow", "Limpiar"))
        self.label_arrival_rate_finite_q_length.setText(_translate("MainWindow", "Tasa de arribos:"))
        self.label_max_queue_length__finite_q_length.setText(_translate("MainWindow", "Tamaño máximo de la cola:"))
        self.btn_view_images_finite_q_length.setText(_translate("MainWindow", "Ver imágenes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_q_finite_length), _translate("MainWindow", "Cola finita"))
        self.label_population_size_finite_population.setText(_translate("MainWindow", "Tamaño máximo de la población:"))
        self.btn_clear_finite_population.setText(_translate("MainWindow", "Limpiar"))
        self.label_num_servers_finite_population.setText(_translate("MainWindow", "Número de servidores:"))
        self.label_service_rate_finite_population.setText(_translate("MainWindow", "Tasa de servicio:"))
        self.label_arrival_rate_finite_population.setText(_translate("MainWindow", "Tasa de arribos:"))
        self.btn_simulate_finite_population.setText(_translate("MainWindow", "Simular"))
        self.btn_view_images_finite_population.setText(_translate("MainWindow", "Ver imágenes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_population_finite), _translate("MainWindow", "Población finita"))
        self.btn_simulate_mg1.setText(_translate("MainWindow", "Simular"))
        self.label_average_service_time_mg1.setText(_translate("MainWindow", "Tiempo promedio de servicio:"))
        self.label_standard_dev_mg1_2.setText(_translate("MainWindow", "Desvío estándar del tiempo de servicio:"))
        self.btn_clear_mg1.setText(_translate("MainWindow", "Limpiar"))
        self.label_standard_dev_mg1.setText(_translate("MainWindow", "Tasa de arribos:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mg1), _translate("MainWindow", "M/G/1"))
        self.btn_simulate_mm1.setText(_translate("MainWindow", "Simular"))
        self.label_service_rate_mm1.setText(_translate("MainWindow", "Tasa de servicio:"))
        self.btn_clear_mm1.setText(_translate("MainWindow", "Limpiar"))
        self.label_arrival_rate_mm1.setText(_translate("MainWindow", "Tasa de arribos:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mm1), _translate("MainWindow", "M/M/1"))
        self.label_settings_round.setText(_translate("MainWindow", "Redondeo (cifras):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("MainWindow", "Ajustes"))
        self.label_results.setText(_translate("MainWindow", "Esperando simulación..."))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
