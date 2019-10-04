import java.io.File;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ChangeFIleExtension {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 System.out.println(
		        renameFileExtension("C:\\Users\\Admin\\Desktop\\hello.pdf", "png"));
	}
	public static boolean renameFileExtension
	  (String filePath, String newExtension)
	  {
	    String target;
	    String currentExtension = getFileExtension(filePath);

	    if (currentExtension.equals("")){
	      target = filePath + "." + newExtension;
	    }
	    else {
	      target = filePath.replaceFirst(Pattern.quote("." +
	          currentExtension) + "$", Matcher.quoteReplacement("." + newExtension));

	    }
	    return new File(filePath).renameTo(new File(target));
	  }
	public static String getFileExtension(String f) {
	    String ext = "";
	    int i = f.lastIndexOf('.');
	    if (i > 0 &&  i < f.length() - 1) {
	      ext = f.substring(i + 1);
	    }
	    return ext;
	  }

}
