package fp.examenes;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class CalendarioExamenes {
	private List<Examen> examenes;

	public CalendarioExamenes(Stream<Examen> examenes) {
		this.examenes = examenes.toList();	
	}
	
	public List<Examen> getExamenes() {
		return new ArrayList<>(examenes);
	}

	public Integer getNumeroExamenes() {
		return examenes.size();
	}

	public String toString() {
		return "CalendarioExamenes [examenes=" + examenes + "]";
	}
	
	
	
	
}
