import customtkinter as ctk



class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.language = "English"
        self.gpa_scale = "12"
        self.cgpa_rows = []
        self.component_rows = []
        self.cgpa_data = []
        self.current_page = "main"

        self.texts = {
            "English": {
                "menu_title": "Face your uni reality",
                "cgpa": "📊 CGPA Calculator",
                "course": "📝 Course Calculator",
                "settings": "⚙️ Settings",
                "back": "← Back",
                "cgpa_title": "CGPA Calculator",
                "add_course": "+ Add Course",
                "course_name": "Course Name",
                "credit": "Credits",
                "grade": "Grade",
                "delete": "Delete",
                "current_cgpa": "Current CGPA",
                "settings_title": "Settings",
                "language": "Language",
                "gpa_scale": "GPA Display Scale",
                "course_title": "Let's see if you will fail or not",
                "target": "Target / Pass Score Wanted:",
                "add_item": "+ Add Item",
                "item": "Item",
                "weight": "Weight %",
                "score": "Score %",
                "status": "Status",
                "done": "Done",
                "pending": "Pending",
                "score_error": "Score Error",
                "current_score": "Current Score",
                "completed_weight": "Completed Weight",
                "save": "💾 Save Data",
                "load": "📂 Load Data",
                "save_success": "Data saved successfully!",
                "load_success": "Data loaded successfully!",
                "error": "Error",
            },
            "繁體中文": {
                "menu_title": "大學生的惡夢",
                "cgpa": "📊 CGPA 計算",
                "course": "📝 單堂課試算",
                "settings": "⚙️ 設定",
                "back": "← 返回",
                "cgpa_title": "大學戰績展示：CGPA 計算",
                "add_course": "+ 新增課堂",
                "course_name": "課程名稱(不填也行)",
                "grade": "成績",
                "delete": "刪除",
                "current_cgpa": "當前 CGPA",
                "settings_title": "設定",
                "language": "語言",
                "gpa_scale": "GPA 顯示方式",
                "course_title": "難道算成績時數學會變得特別好嗎？",
                "target": "目標分數 / Pass 分數:",
                "add_item": "+ 新增項目",
                "item": "項目",
                "weight": "權重 %",
                "score": "分數 %",
                "status": "完成情況",
                "done": "已完成",
                "pending": "未完成",
                "score_error": "分數錯誤",
                "current_score": "目前已拿總分",
                "completed_weight": "已完成權重",
                "save": "💾 儲存檔案",
                "load": "📂 讀取檔案",
                "save_success": "儲存成功！",
                "load_success": "讀取成功！",
                "error": "發生錯誤",
            }
        }

        self.title("大學鹹魚升級指南")
        self.geometry("300x450")
        self.resizable(False, False)

        self.main_menu()

    def t(self, key):
        return self.texts[self.language][key]

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.sync_data_to_memory()
        self.current_page = "main"
        self.clear_window()
        self.geometry("300x450")

        ctk.CTkLabel(self, text=self.t("menu_title"), font=("Arial", 20, "bold")).pack(pady=40)

        ctk.CTkButton(self, text=self.t("cgpa"), command=self.cgpa_page).pack(pady=10)
        ctk.CTkButton(self, text=self.t("course"), command=self.course_page).pack(pady=10)
        ctk.CTkButton(self, text=self.t("settings"), command=self.settings_page).pack(pady=10)

        buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        buttons_frame.pack(pady=30)
        ctk.CTkButton(buttons_frame, text=self.t("save"), width=120, command=self.save_file).pack(side="left", padx=10)
        ctk.CTkButton(buttons_frame, text=self.t("load"), width=120, command=self.load_file).pack(side="right", padx=10)

    # =========================
    # CGPA PAGE
    # =========================
    def cgpa_page(self):
        self.sync_data_to_memory()
        self.current_page = "cgpa"
        self.clear_window()
        self.geometry("650x600")
        self.cgpa_rows = []

        ctk.CTkButton(self, text=self.t("back"), width=100, command=self.main_menu).pack(
            anchor="nw", padx=10, pady=10
        )

        ctk.CTkLabel(self, text=self.t("cgpa_title"), font=("Arial", 24, "bold")).pack(pady=10)

        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkButton(
            header_frame,
            text=self.t("add_course"),
            width=120,
            command=self.add_cgpa_row
        ).pack(side="right", padx=10)

        title_bar = ctk.CTkFrame(self, height=30, fg_color="#EBB973")
        title_bar.pack(fill="x", padx=20)

        ctk.CTkLabel(title_bar, text=self.t("course_name"), width=380).grid(row=0, column=0, padx=5)
        ctk.CTkLabel(title_bar, text=self.t("grade"), width=120).grid(row=0, column=2, padx=5)
        ctk.CTkLabel(title_bar, text=self.t("delete"), width=80).grid(row=0, column=3, padx=5)

        self.cgpa_scroll = ctk.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent")
        self.cgpa_scroll.pack(fill="both", expand=True, padx=20, pady=5)

        self.result_label = ctk.CTkLabel(
            self,
            text=f"{self.t('current_cgpa')}: 0.00 / 12.00",
            font=("Arial", 20, "bold")
        )
        self.result_label.pack(pady=15)

        if self.cgpa_data:
            for row_data in self.cgpa_data:
                self.add_cgpa_row(default_name=row_data.get("name", ""), default_grade=row_data.get("grade", "A"), calculate=False)
            self.calculate_cgpa()
        else:
            self.add_cgpa_row()

    def add_cgpa_row(self, default_name="", default_grade="A", calculate=True):
        row_frame = ctk.CTkFrame(self.cgpa_scroll, fg_color="transparent")
        row_frame.pack(fill="x", pady=5)

        name_entry = ctk.CTkEntry(row_frame, placeholder_text="Course")
        if default_name:
            name_entry.insert(0, default_name)
        name_entry.grid(row=0, column=0, padx=5, sticky="ew")

        # Grade List
        grade_menu = ctk.CTkOptionMenu(
            row_frame,
            values=["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"],
            command=lambda _: self.calculate_cgpa()
        )
        grade_menu.set(default_grade)
        grade_menu.grid(row=0, column=2, padx=5)

        # 刪除鍵
        delete_btn = ctk.CTkButton(
            row_frame,
            text="X",
            width=50,
            fg_color="#8B0000",
            command=lambda: self.delete_cgpa_row(row_frame)
        )
        delete_btn.grid(row=0, column=3, padx=5)

        row_frame.grid_columnconfigure(0, weight=1)

        self.cgpa_rows.append({
            "frame": row_frame,
            "name": name_entry,
            "grade": grade_menu
        })

        if calculate:
            self.calculate_cgpa()

    # 刪一欄
    def delete_cgpa_row(self, frame):
        self.cgpa_rows = [row for row in self.cgpa_rows if row["frame"] != frame]
        frame.destroy()
        self.calculate_cgpa()

    def calculate_cgpa(self):
        scale_12 = {
            "A+": 12, "A": 11, "A-": 10,
            "B+": 9, "B": 8, "B-": 7,
            "C+": 6, "C": 5, "C-": 4,
            "D+": 3, "D": 2, "D-": 1,
            "F": 0
        }
        
        scale_4 = {
            "A+": 4, "A": 3.9, "A-": 3.7,
            "B+": 3.3, "B": 3, "B-": 2.7,
            "C+": 2.3, "C": 2, "C-": 1.7,
            "D+": 1.3, "D": 1, "D-": 0.7,
            "F": 0
        }

        result = 0 ## 總分
        ctr = 0 ## 有幾科

        # 12 scale的gpa
        for row in self.cgpa_rows:
            grade = row["grade"].get()

            result += scale_12[grade]
            ctr += 1
        
        cgpa_12 = result / ctr if ctr > 0 else 0
        
        # reset
        ctr, result = 0, 0
        
        # 4 scale的gpa
        for row in self.cgpa_rows:
            grade = row["grade"].get()

            result += scale_4[grade]
            ctr += 1

        cgpa_4 = result / ctr if ctr > 0 else 0

        # 更改版面
        if self.gpa_scale == "12":
            text = f"{self.t('current_cgpa')}: {cgpa_12:.2f} / 12.00"
        elif self.gpa_scale == "4":
            text = f"{self.t('current_cgpa')}: {cgpa_4:.2f} / 4.00"
        else:
            text = f"{self.t('current_cgpa')}: {cgpa_12:.2f} / 12.00  |  {cgpa_4:.2f} / 4.00"

        self.result_label.configure(text=text)

    # =========================
    # COURSE
    # =========================
    def course_page(self):
        self.sync_data_to_memory()
        self.current_page = "course"
        self.clear_window()
        self.geometry("650x600")
        self.component_rows = []

        ctk.CTkButton(self, text=self.t("back"), width=100, command=self.main_menu).pack(
            anchor="nw", padx=10, pady=10
        )

        ctk.CTkLabel(self, text=self.t("course_title"), font=("Arial", 24, "bold")).pack(pady=10)

        control_frame = ctk.CTkFrame(self)
        control_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(control_frame, text=self.t("target")).pack(side="left", padx=5)

        self.target_entry = ctk.CTkEntry(control_frame, width=80, placeholder_text="50")
        self.target_entry.insert(0, "50")
        self.target_entry.pack(side="left", padx=5)

        ctk.CTkButton(control_frame, text=self.t("add_item"), command=self.add_component_row).pack(
            side="right", padx=5
        )

        title_bar = ctk.CTkFrame(self, fg_color="#EBB973")
        title_bar.pack(fill="x", padx=20)

        ctk.CTkLabel(title_bar, text=self.t("item"), width=250).grid(row=0, column=0, padx=5)
        ctk.CTkLabel(title_bar, text=self.t("weight"), width=110).grid(row=0, column=1, padx=5)
        ctk.CTkLabel(title_bar, text=self.t("score"), width=95).grid(row=0, column=2, padx=5)
        ctk.CTkLabel(title_bar, text=self.t("status"), width=30).grid(row=0, column=3, padx=5)
        ctk.CTkLabel(title_bar, text=self.t("delete"), width=50).grid(row=0, column=4, padx=5)

        self.component_scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.component_scroll.pack(fill="both", expand=True, padx=20, pady=5)

        self.course_result_label = ctk.CTkLabel(
            self,
            text=f"{self.t('current_score')}: 0.00 / 100",
            font=("Arial", 18, "bold")
        )
        self.course_result_label.pack(pady=5)

        self.need_label = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.need_label.pack(pady=10)

        self.target_entry.bind("<KeyRelease>", lambda e: self.calculate_course())

        self.add_component_row("Assignment", "10", calculate=False)
        self.add_component_row("Quiz", "10", calculate=False)
        self.add_component_row("Midterm", "30", calculate=False)
        self.add_component_row("Final", "50", "", calculate=False)
        self.calculate_course()

    def add_component_row(self, default_name="", default_weight="", default_score="", calculate=True):
        row_frame = ctk.CTkFrame(self.component_scroll, fg_color="transparent")
        row_frame.pack(fill="x", pady=5)

        name_entry = ctk.CTkEntry(row_frame, placeholder_text="Assignment / Quiz / Midterm / Final")
        name_entry.insert(0, default_name)
        name_entry.grid(row=0, column=0, padx=5, sticky="ew")

        weight_entry = ctk.CTkEntry(row_frame, width=100, placeholder_text="20")
        weight_entry.insert(0, default_weight)
        weight_entry.grid(row=0, column=1, padx=5)

        score_entry = ctk.CTkEntry(row_frame, width=100, placeholder_text="blank = unknown")
        score_entry.insert(0, default_score)
        score_entry.grid(row=0, column=2, padx=5)

        status_label = ctk.CTkLabel(row_frame, text=self.t("pending"))
        status_label.grid(row=0, column=3, padx=5)

        delete_btn = ctk.CTkButton(
            row_frame,
            text="X",
            width=50,
            fg_color="#8B0000",
            command=lambda: self.delete_component_row(row_frame)
        )
        delete_btn.grid(row=0, column=4, padx=5)

        row_frame.grid_columnconfigure(0, weight=1)

        self.component_rows.append({
            "frame": row_frame,
            "name": name_entry,
            "weight": weight_entry,
            "score": score_entry,
            "status": status_label
        })

        weight_entry.bind("<KeyRelease>", lambda e: self.calculate_course())
        score_entry.bind("<KeyRelease>", lambda e: self.calculate_course())
        name_entry.bind("<KeyRelease>", lambda e: self.calculate_course())

        if calculate:
            self.calculate_course()

    def delete_component_row(self, frame):
        self.component_rows = [row for row in self.component_rows if row["frame"] != frame]
        frame.destroy()
        self.calculate_course()

    def calculate_course(self):
        current_score = 0
        completed_weight = 0
        unknown_weight = 0
        total_weight = 0

        try:
            target = float(self.target_entry.get())
        except ValueError:
            target = 50

        for row in self.component_rows:
            try:
                weight = float(row["weight"].get())
            except ValueError:
                weight = 0

            score_text = row["score"].get().strip()
            total_weight += weight

            if score_text == "":
                unknown_weight += weight
                row["status"].configure(text=self.t("pending"))
            else:
                try:
                    score = float(score_text)
                    current_score += weight * score / 100
                    completed_weight += weight
                    row["status"].configure(text=self.t("done"))
                except ValueError:
                    row["status"].configure(text=self.t("score_error"))

        self.course_result_label.configure(
            text=f"{self.t('current_score')}: {current_score:.2f} / 100    "
                 f"{self.t('completed_weight')}: {completed_weight:.1f}%"
        )

        if self.language == "English":
            warning = f"⚠️ Total weight = {total_weight:.1f}%, how is that possible? Bonus?\n" if total_weight != 100 else ""

            if unknown_weight <= 0:
                if current_score >= target:
                    msg = f"{warning}✅ Final score is {current_score:.2f}. Congratulations YAAA!!"
                else:
                    msg = f"{warning}❌ Final score is {current_score:.2f}. Study or you're cooked."
            else:
                needed = target - current_score

                if needed <= 0:
                    msg = f"{warning} You already had enough mark to pass!"
                elif needed > 100:
                    msg = f"{warning} Need {needed:.2f}% more on remaining items and it's impossible. You are cooked."
                else:
                    msg = f"{warning} Need {needed:.2f}% average on remaining items to reach {target:.1f}. Good luck!"
        else:
            warning = f"目前總 weight = {total_weight:.1f}%，難道不是 100% 嗎？\n" if total_weight != 100 else ""

            if unknown_weight <= 0:
                if current_score >= target:
                    msg = f"{warning}✅ 最終分數: {current_score:.2f}，恭喜達成目標！"
                else:
                    msg = f"{warning}❌ 最終分數: {current_score:.2f}，還不去讀書！還是已經考完啦？"
            else:
                needed = target - current_score

                if needed <= 0:
                    msg = f"{warning} 維持現狀一樣能達標，你是天才！"
                elif needed > 100:
                    msg = f"{warning} 兄弟你有格子沒填"
                else:
                    msg = f"{warning} 還需要 {needed:.2f}%，加油歐別玩了。"

        self.need_label.configure(text=msg)

    # =========================
    # SETTINGS PAGE
    # =========================
    def settings_page(self):
        self.sync_data_to_memory()
        self.current_page = "settings"
        self.clear_window()
        self.geometry("400x350")

        ctk.CTkButton(self, text=self.t("back"), width=100, command=self.main_menu).pack(
            anchor="nw", padx=10, pady=10
        )

        ctk.CTkLabel(self, text=self.t("settings_title"), font=("Arial", 24, "bold")).pack(pady=20)

        ctk.CTkLabel(self, text=self.t("language")).pack(pady=(10, 5))

        language_menu = ctk.CTkOptionMenu(
            self,
            values=["English", "繁體中文"],
            command=self.change_language
        )
        language_menu.set(self.language)
        language_menu.pack(pady=5)

        ctk.CTkLabel(self, text=self.t("gpa_scale")).pack(pady=(20, 5))

        scale_menu = ctk.CTkOptionMenu(
            self,
            values=["12", "4", "Both"],
            command=self.change_gpa_scale
        )
        scale_menu.set(self.gpa_scale)
        scale_menu.pack(pady=5)

    def change_language(self, value):
        self.language = value
        self.settings_page()

    def change_gpa_scale(self, value):
        self.gpa_scale = value

    def sync_data_to_memory(self):
        if getattr(self, 'current_page', 'main') == "cgpa":
            self.cgpa_data = []
            for row in self.cgpa_rows:
                try:
                    self.cgpa_data.append({
                        "name": row["name"].get(),
                        "grade": row["grade"].get()
                    })
                except Exception:
                    pass

    def save_file(self):
        import json
        from tkinter import filedialog, messagebox
        
        self.sync_data_to_memory()
        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not filepath:
            return

        data = {
            "language": self.language,
            "gpa_scale": self.gpa_scale,
            "cgpa_data": self.cgpa_data
        }
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            messagebox.showinfo(self.t("save_success"), self.t("save_success"))
        except Exception as e:
            messagebox.showerror(self.t("error"), str(e))

    def load_file(self):
        import json
        from tkinter import filedialog, messagebox
        
        filepath = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not filepath:
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if "language" in data:
                self.language = data["language"]
            if "gpa_scale" in data:
                self.gpa_scale = data["gpa_scale"]
            if "cgpa_data" in data:
                self.cgpa_data = data["cgpa_data"]
                
            messagebox.showinfo(self.t("load_success"), self.t("load_success"))
            self.main_menu()
        except Exception as e:
            messagebox.showerror(self.t("error"), str(e))


if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()